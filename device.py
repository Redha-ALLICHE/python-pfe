import telnetlib as tn
from db import Utility
import time

class Device(Utility): 
    """this class models a device like routers ,swithes and servers """

    def __init__(self,devices_list='list_of_devices.json'):
        """declare the variables neeeded to specify a device and get the devices_list file path where this informations are stored """

        self.myDb = Utility(devices_list)
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

    def login(self, refreshing =True):
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
            if answer.endswith(">") :
                if self.data["name"] != answer[2:-1] and refreshing:
                    self.data["name"] = answer[2:-1]
                    self.myDb.refreshSetting(self.data, self.data["id"])
                print("Connection successful to " + self.data["ip_address"])
                return target
            else:
                print("Failed to connect to "+ self.data["ip_address"])
                return None

    def loginPrivelegeMode(self, target, enablePassword):
        """login to privelege mode in a cisco device"""
        if target:
            target.write(("en\n").encode())
            time.sleep(0.2)
            target.write((enablePassword).encode())
            answer = target.read_some().decode()
            if answer.endswith("#"):
                return target
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
            print("Commands did not apply!!")
        return None
            
    def configureMultipleFromRange(self, start, end, command_path="list_of_commands.txt", save=False):
        """configure a range of ips with the same configuration"""
        self.data["username"] = input("give me the username : ")
        self.data["password"] = input("give me the password : ")
        for ip in self.myDb.generateRange(start,end):
            self.data["ip_address"] = ip 
            self.executeCommands(self.login(refreshing=save), command_path)
        return None

    def configureMultipleFromFile(self, ip_path="list_of_ip.txt", command_path="list_of_commands.txt", save=False):
        """configure a range of ips retrieved from a file with the same configuration"""
        file = self.myDb.openFile(ip_path)
        if file:
            self.data["username"] = input("give me the username : ")
            self.data["password"] = input("give me the password : ")
            for ip in file:
                self.data["ip_address"] = ip
                self.executeCommands(self.login(refreshing=save), command_path)
            file.close()
        return None
        
