import getpass
from network_db.net_database import Net_db
import time
import shutil
import subprocess


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

    def getList(self, path):
        """converts a file to a list and returns it"""
        with open(path) as file:
            lines = file.readlines()
        return lines

    def getfiles(self, folder):
        """get the names of the files in the folder"""
        return shutil.os.listdir(folder)

    def prepareBackup(self, ip, root, data, temp):
        """get the config and store it to a file """
        name = str(root) + str(ip) + time.strftime('_%d_%m_%Y_%Hh%M.conf',time.localtime())
        with open(name, mode='w') as f:
            temp[2].emit("Saving the configuration in the file : " + name + '\n')
            f.write("\n".join(data.split("\n")[3:-2]))
        return name

    def getRestore(self, actual_config, recovery_config):
        """return the applicable config to do the restore """
        new_config = []
        for x ,line in enumerate(actual_config):
            line = line.rstrip('\r')
            if line.startswith('aaa'):
                pass
            elif line in recovery_config or line.startswith('!') or x <= 4:
                new_config.append(line)
            elif line.startswith('no '):
                new_config.append(line.lstrip('no '))
            else:
                new_config.append('no ' + line)
        final = ['\n'.join(new_config), recovery_config]
        return  final            

    def mktemp(self, temp_path):
        """creates the temp_new folder"""
        try:
            name = temp_path + '_new/'
            shutil.os.mkdir(name)
        except:
            print(name)
        return name

    def removeTemp(self, new_path, root_path='temp/'):
        """remove the content of the temp folder"""
        try:
            shutil.rmtree(root_path, ignore_errors=True )
            shutil.copytree(new_path, root_path)
            shutil.rmtree(new_path, ignore_errors=True)
        except:
            print("error while cleaning the temp !!")

    def fillData(self, data):
        """retrieve the information from the user about a new device and store it in the data variable """
        what_needed = ['host', 'device_type','type', 'ip', 'username']
        for element in what_needed:
            data[element] = input("Give me the " + element + ' : ')
        data["password"] = getpass.getpass("Give me the password :")
        data["secret"] = getpass.getpass("Give me the enable password :")
        data['description'] = input('Give me the description : ')
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

    def refreshDevice(self, data, temp):
        """update the settings of one existing device in your devices database"""
        db = Net_db()
        check = self.searchDevice(data)
        if check != "EOL":
            db.updateDevice(data)
            temp[2].emit("Refreshing the existing info of the device\n")
            db.saveDb()
            db.closeDb()
            return self.all_info[check]
        else:
            self.all_info.append(data)
            db.addDevice(data)
            db.saveDb()
            db.closeDb()
            temp[2].emit("Adding the device with the ip address " + data["ip"] + " in the list of devices\n")
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
            data["username"] = input("Enter the username : ")
            data["password"] = getpass.getpass("Enter the password : ")
            data["type"] = input("Enter the type : ")
        elif mode == "check":
            index = self.searchDevice(data)
            if index != "EOL" and self.all_info[index]["username"] and self.all_info[index]["password"]:
                print("Found login informations")
                data = self.all_info[index].copy()
            else:
                data["username"] = input("Enter the username : ")
                data["password"] = getpass.getpass("Enter the password : ")
                data["type"] = input("Enter the type : ")
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
    
    def ping(self, host):
        """
        Returns True if host (str) responds to a ping request.
        Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
        """
        # Ping command count option as function of OS
        param = '-n 1 ' if subprocess.sys.platform.lower().startswith("win") else '-c 1 '
        
        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, str(host)]
        # Pinging
        s = subprocess.call(command)
        return s == 0
