import json

class Database():
    """this class ensures the access to the database""" 
    def __init__(self, devices_file):
        self.devices_file = devices_file

    def __len__(self):
        """return the number of item in the file"""
        data = self.getAllInfo()
        if data:
            return len(data)
        return 0

    def openFile(self, path, mode='r'):
        """opens the file and returns the pointer"""
        try:
            return open(path, mode)
        except FileNotFoundError :
            print("file not found")
            return None
        
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

    def getItemByName(self, the_name=''):
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
        info = self.getItemByName(the_name=dev_name)
        if info:
            all_info = self.getAllInfo()
            all_info.remove(info)
            with open(self.devices_file, 'w') as destination:
                json.dump(all_info, destination, indent=4)
            print("deleting done")
        return None

    def refreshSetting(self, data, id):
        """update the settings of one existing device in your list of devices file"""
        id = int(id)
        all_info = self.getAllInfo()
        if len(all_info) > id:
            all_info[id] = data
            with open(self.devices_file, 'w') as destination:
                json.dump(all_info, destination, indent=4)
            print("refreshing the name of the device")
            return all_info[id]
        print("Error !!! the device with the id = " + id + " is not found in the file")
        return None
        
