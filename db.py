import json

class Database():
    """this class ensures the access to the database""" 
    def __init__(self, devices_file):
        self.devices_file = devices_file
        pass
    
    def getAllInfo(self):
        """retrieve all the devices informations from the .json file"""
        try:
            with open(self.devices_file) as destination:
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
                print("Error !!! the device " + the_name + " is not found in the file")
            return None

    def addDevice(self, data):
        """add the informations about the device in the devices_list.json file """
        """amélioaration du point de vu storage """
        try:
            with open(self.devices_file, 'r') as destination:
                print("saving your data...")
        except FileNotFoundError:
            print("Warning !! the file  does't exists ")
            with open(self.devices_file, 'w') as destination:
                json.dump([data], destination, indent=4)
        else:
            info = self.getAllInfo()
            info.append(data)
            with open(self.devices_file, 'w') as destination:
                json.dump(info, destination, indent=4)

    def deleteDevice(self, dev_name=''):
        """delete the device from the file"""
        info = self.getItem(the_name=dev_name)
        if info:
            all_info = self.getAllInfo()
            all_info.remove(info)
            with open(self.devices_file, 'w') as destination:
                json.dump(all_info, destination, indent=4)
            print("deleting done")
        return None
