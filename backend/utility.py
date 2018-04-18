import getpass
from network_db.net_database import Net_db

class Utility():
    """this class ensures the access to the files and prove some utility functions""" 
    def __init__(self):
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

    def fillData(self, data):
        """retrieve the information from the user about a new device and store it in the data variable """
        what_needed = ['host', 'device_type', 'ip', 'username']
        for element in what_needed:
            data[element] = input("Give me the " + element + ' : ')
        data["password"] = getpass.getpass("Give me the password :")
        data["secret"] = getpass.getpass("Give me the enable password :")
        return data

    def refreshTheDb(self):
        """stores the new all info in the list of devices database"""
        db = Net_db()
        for item in self.all_info:
            db.updateDevice(item)
        db.saveDb()
        db.closeDb()

    def getAllInfo(self):
        """retrieve all the devices informations from the database"""
        db = Net_db()
        allData = db.getAll()
        db.closeDb()
        return allData

    def getItemByName(self, the_name=''):
            """retrieve the informations about a device from the database """
            if self.all_info:
                for item in self.all_info:
                    if item["host"] == the_name:
                        return item
                print("Error !!! the device " + the_name + " is not found in the file")
            return None

    def deleteDevice(self, dev_name=''):
        """delete the device from the file"""
        info = self.getItemByName(the_name=dev_name)
        if info:
            self.all_info.remove(info)
            db = Net_db()
            db.deleteDevice(info["ip"])
            db.saveDb()
            db.closeDb()
            print("deleting done")
        return None

    def refreshSetting(self, data):
        """update the settings of one existing device in your devices database"""
        db = Net_db()
        check = self.searchDevice(data)
        if check != "EOL":
            db.updateDevice(data)
            print("Refreshing the existing info of the device")
            db.saveDb()
            db.closeDb()
            return self.all_info[check]
        else:
            self.all_info.append(data)
            db.addDevice(data)
            db.saveDb()
            db.closeDb()
            print("Adding the device with the ip address " + data["ip"] + " in the list of devices")
            return None

    def searchDevice(self, data):
        """retrun the index of the device if found in the file"""
        for i, item in enumerate(self.all_info, 0):
            if item["ip"] == data["ip"]:
                return i
        return "EOL"

    def getInputs(self, data, mode="one"):
        """prompt the login inputs for two modes :ask or check """ 
        if mode == "ask":
            print((" Trying to connect to " + data["ip"]+' ').center(80,"#"))
            data["username"] = input("Enter the username : ")
            data["password"] = getpass.getpass("Enter the password : ")
        elif mode == "check":
            print((" Trying to connect to " + data["ip"]+' ').center(80,"#"))
            index = self.searchDevice(data)
            if index != "EOL" and self.all_info[index]["username"] and self.all_info[index]["password"]:
                print("Found login informations")
                data = self.all_info[index].copy()
                print(data)
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
    
