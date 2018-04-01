import json
import telnetlib as tn
from db import Database

class Device(Database): 
    """this class models a device like routers ,swithes and servers """

    def __init__(self,devices_list='list_of_devices.json'):
        """declare the variables neeeded to specify a device and get the devices_list file path where this informations are stored """

        self.myDb = Database(devices_list)
        self.data = {'id':'0','name':'','type':'','ip_address':'','port':'23','username':'','password':''} 

    def getInputFromUser(self):
        """retrieve the information from the user about a new device and store it in the data variable """
        for element in self.data.keys():
            self.data[element] = input("give me the " + element + ' : ')
      
    def show_info(self):
        """print on the screen the informations about the device """
        print(self.data)


    def login(self):
        """enable to login to the device """
        try:
            print("loading...")
            target = tn.Telnet().open(host=self.data['ip_address'], port=self.data['port'])
        except TimeoutError:
            print("Error !!! device unreacheable ")
            return None
        else:
            target.read_until("username: ")
            target.write(self.data['username'] + "\n")
            target.read_until("Password: ")
            target.write(self.data['password'] + "\n")
            print(target.read_all())
            target.write("exit\n")
            tn.Telnet().close()


    

