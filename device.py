import json
import telnetlib as tn

class Device():
    """this class models a device like routers ,swithes and servers """

    def __init__(self,devices_list='list_of_devices.json'):
        """declare the variables neeeded to specify a device and get the devices_list file path where this informations are stored """
        self.path = devices_list
        self.data = {'id':'0','name':'','type':'','ip_address':'','port':'23','username':'','password':''} 

    def getInputFromUser(self):
        """retrieve the information from the user about a new device and store it in the data variable """
        for element in self.data.keys():
            self.data[element] = input("give me the " + element + ' : ')

    def getAllInfo(self):
        """retrieve all the devices informations from the .json file""" 
        try:
            with open(self.path) as destination:
                return json.load(destination)
        except FileNotFoundError:
            print("Error !!! the file does't exists ")
            return None
        except json.JSONDecodeError:
            print("Error !!! the file is corrupted")
            return None

    def getItem(self, the_name=''):
        """retrieve the informations about a device from the list_of_devices.json file """
        all_info = self.getAllInfo()
        if all_info:
            for item in all_info:
                if item["name"] == the_name:
                    self.data = item
                    return item
            print("Error !!! the device is not found in the file")
        return None
            
    def show_info(self):
        """print on the screen the informations about the device """
        print(self.data)

    def addDevice(self):
        """add the informations about the device in the devices_list.json file """
        try:
            with open(self.path, 'r') as destination:
                print("saving your data...")    
        except FileNotFoundError:
            print("Warning !! the file  does't exists ")
            with open(self.path, 'w') as destination:
                json.dump([self.data], destination, indent=4)
        else:
            info = self.getAllInfo()
            info.append(self.data)
            with open(self.path, 'w') as destination:
                json.dump(info, destination, indent=4)

    def deleteDevice(self, dev_name=''):
        """delete the device from the file"""
        info = self.getItem(the_name=dev_name)
        if info:
            all_info = self.getAllInfo()
            all_info.remove(info)
            with open(self.path, 'w') as destination:
                json.dump(all_info, destination, indent=4)
            print("deleting done")
        return None

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


    

