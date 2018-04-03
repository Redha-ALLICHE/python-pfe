import json
import getpass

class Utility():
    """this class ensures the access to the files and prove some utility functions""" 
    def __init__(self, devices_file):
        self.devices_file = devices_file
        self.all_info = self.getAllInfo()

    def __len__(self):
        """return the number of item in the file"""
        if self.all_info:
            return len(self.all_info)
        return 0

    def openFile(self, path, mode='r'):
        """opens the file and returns the pointer"""
        try:
            return open(path, mode)
        except FileNotFoundError :
            print("file named " + path + " is not found")
            return None

    def refreshTheFile(self):
        """stores the new all info in the list of devices file"""
        with open(self.devices_file, 'w') as destination:
            json.dump(self.all_info, destination, indent=4)

    def getAllInfo(self):
        """retrieve all the devices informations from the .json file"""
        try:
            with open(self.devices_file) as destination:
                return json.load(destination)
        except FileNotFoundError:
            print("Error !!! the file does't exists ")
            if input("To create it write 'y': ").lower() == 'y':
                with open(self.devices_file, 'w') as destination:
                    json.dump([], destination, indent=4)
                return []
            return None
        except json.JSONDecodeError:
            print("Error !!! the file is corrupted")
            return None

    def getItemByName(self, the_name=''):
            """retrieve the informations about a device from the list_of_devices.json file """
            if self.all_info:
                for item in self.all_info:
                    if item["name"] == the_name:
                        return item
                print("Error !!! the device " + the_name + " is not found in the file")
            return None

    def deleteDevice(self, dev_name=''):
        """delete the device from the file"""
        info = self.getItemByName(the_name=dev_name)
        if info:
            self.all_info.remove(info)
            self.refreshTheFile()
            print("deleting done")
        return None

    def refreshSetting(self, data):
        """update the settings of one existing device in your list of devices file"""
        check = self.searchDevice(data)
        if check != "EOL":
            self.all_info[check] = data
            self.refreshTheFile()
            print("Refreshing the existing info of the device")
            return self.all_info[check]
        else:
            self.all_info.append(data)
            self.refreshTheFile()
            print("Adding the device with the ip address " + data["ip_address"] + " in the list of devices")
            return None

    def searchDevice(self, data):
        """retrun the index of the device if found in the file"""
        for i, item in enumerate(self.all_info, 0):
            if item["ip_address"] == data["ip_address"]:
                return i
        return "EOL"

    def getInputs(self, data, mode="one"):
        """prompt the login inputs for two modes :ask or check """ 
        if mode == "ask":
            print((" Trying to connect to " + data["ip_address"]+' ').center(80,"#"))
            data["username"] = input("Enter the username : ")
            data["password"] = getpass.getpass("Enter the password : ")
        elif mode == "check":
            print((" Trying to connect to " + data["ip_address"]+' ').center(80,"#"))
            index = self.searchDevice(data)
            if index != "EOL" and self.all_info[index]["username"] and self.all_info[index]["password"]:
                print("Found login informations")
                data = self.all_info[index]
            else:
                data["username"] = input("Enter the username : ")
                data["password"] = getpass.getpass("Enter the password : ")
        return data

    def generateRange(self, start, end):
        """get a starting ip and an ending ip and generate a list of ips 192.168.1.2-52"""
        ip_list = []
        increment = start
        startSplit = [int(x) for x in start.split('.')]
        endSplit = [int(x) for x in end.split('.')]
        indice = True
        for i in range(0,3):
            if startSplit[i] < endSplit[i]:
                break
            elif startSplit[i] > endSplit[i]:
                indice = False
        if not indice:
            print("Error in the range")
            return None
        while increment != end:
            ip_list.append(increment)
            splitted = [int(x) for x in increment.split('.')]
            if splitted[3] < 255:
                splitted[3] += 1
            elif splitted[2] < 255:
                splitted[3]= 0
                splitted[2]+= 1
            elif splitted[1] < 255:
                splitted[3] = 0
                splitted[2] = 0
                splitted[1]+= 1
            elif splitted[0] < 255:
                splitted[3] = 0
                splitted[2] = 0
                splitted[1] = 0
                splitted[0] += 1
            else:
                return None
            increment = ".".join([str(x) for x in splitted])
        ip_list.append(end)
        return ip_list
    
