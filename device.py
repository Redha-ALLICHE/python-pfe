import telnetlib as tn
from db import Database
import time

class Device(Database): 
    """this class models a device like routers ,swithes and servers """

    def __init__(self,devices_list='list_of_devices.json'):
        """declare the variables neeeded to specify a device and get the devices_list file path where this informations are stored """

        self.myDb = Database(devices_list)
        self.data = {'id':'0','name':'','type':'','ip_address':'','port':'23','username':'','password':''} 

    def getInputFromUser(self):
        """retrieve the information from the user about a new device and store it in the data variable """
        what_needed = ['name', 'type', 'ip_address', 'username' , 'password']
        for element in what_needed:
            self.data[element] = input("give me the " + element + ' : ')
        self.data["id"] = len(self.myDb)

    def show_info(self):
        """print on the screen the informations about the device """
        print(self.data)

    def setData(self, newData):
        """the setter of data"""
        if newData:
            self.data = newData
        else:
            return None

    def login(self):
        """enable the user to login into the device """
        try:
            if self.data["ip_address"] =="":
                return None
            print("loading...")
            target = tn.Telnet()
            target.open(host=self.data['ip_address'], port=self.data['port'])
        except (TimeoutError, OSError):
            print("Error !!! device unreacheable ")
            return None
        else:
            target.read_until("Username: ".encode())
            target.write((self.data['username'] + "\n").encode())
            target.read_until("Password: ".encode())
            target.write((self.data['password'] + "\n").encode())
            answer = target.read_some().decode()
            if answer.endswith(">"):
                if self.data["name"] != answer[2:-1]:
                    self.data["name"] = answer[2:-1]
                    self.myDb.refreshSetting(self.data, self.data["id"])
                print("Connection successful to " + self.data["name"])
                return target
            else:
                print("Connection failed")
                return None

    def executeCommands(self, target, the_file="list_of_commands.txt"):
        """execute commands from a file into one device"""
        file = self.myDb.openFile(the_file)
        if target and file:
            for command in file:
                target.write((command + '\n').encode())
                time.sleep(0.2)
            target.write(("exit\n").encode())
            print(target.read_all().decode())
            target.close()
            file.close()
        else:
            print("Nothing to do !!")
        return None
            

        

    

