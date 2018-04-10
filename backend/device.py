import telnetlib as tn
from db import Utility
import time
import getpass
import paramiko as pk

class Device(Utility): 
    """this class models a device like routers ,swithes and servers """

    def __init__(self,devices_list='list_of_devices.json'):
        """declare the variables neeeded to specify a device and get the devices_list file path where this informations are stored """
        self.myDb = Utility(devices_list)
        self.data = {'name':'','type':'','ip_address':'','port':'23','username':'','password':''} 

    def getInputFromUser(self):
        """retrieve the information from the user about a new device and store it in the data variable """
        self.data = self.myDb.fillData(self.data)

    def show_info(self):
        """print on the screen the informations about the device """
        print(self.data)

    def setData(self, newData):
        """the setter of data"""
        if newData:
            self.data = newData
        else:
            return None

    """Telnet part"""

    def loginTelnet(self, refreshing =True, privelege=False):
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
            self.executeLine(target, self.data["username"])
            target.read_until("Password: ".encode())
            self.executeLine(target, self.data["password"])
            answer = target.read_some().decode()
            if answer.endswith(">") :
                if self.data["name"] != answer[2:-1] and refreshing:
                    self.data["name"] = answer[2:-1]
                    self.myDb.refreshSetting(self.data)
                print("Connection successful to " + self.data["ip_address"])
                if privelege:
                    return self.loginPrivelegeMode(target)
                return target
            else:
                print("Failed to connect to "+ self.data["ip_address"])
                return None

    def loginPrivelegeMode(self, target):
        """login to privelege mode in a cisco device"""
        if target:
            enablePassword = getpass.getpass("Input the enable password : ")
            self.executeLine(target,"en")
            self.executeLine(target,enablePassword)
            answer = target.read_some().decode()
            if answer.endswith("#"):
                print("Getting into the privelege mode")
                return target
            else:
                print("incorrect password",end=' ')
                target.close()
                return None

    def executeCommands(self, target, the_file="list_of_commands.txt",silent= True):
        """execute commands from a file into one device"""
        file = self.myDb.openFile(the_file)
        if target and file:
            self.executeLine(target,"terminal lengh 0")
            for command in file:
                self.executeLine(target,command)
            self.executeLine(target,"exit")
            if silent:
                print("All the commands are done")
            else:
                print(target.read_all().decode())
            target.close()
            file.close()
        else:
            print("Commands did not apply!!")
        return None
        
    def executeLine(self, target, command):
        """executes a line of command in the target"""
        target.write((command + '\n').encode())
        time.sleep(0.2)
        return target

    def configureMultipleFromRange(self, start, end, command_path="list_of_commands.txt", save=False, silent=True, privelege=False, mode="one"):
        """configure a range of ips with the same configuration"""
        if mode == "one":
            print("Enter the common login")
            self.data = self.myDb.getInputs(self.data, mode='ask')
        for ip in self.myDb.generateRange(start,end):
            self.data["ip_address"] = ip
            self.data = self.myDb.getInputs(self.data, mode= mode)
            self.executeCommands(self.loginTelnet(refreshing=save,privelege=privelege),command_path, silent=True)
        return None

    def configureMultipleFromFile(self, ip_path="list_of_ip.txt", command_path="list_of_commands.txt", save=False, silent=True, privelege=False, mode='one'):
        """configure a range of ips retrieved from a file with the same configuration"""
        file = self.myDb.openFile(ip_path)
        if mode == 'one':
            print("Enter the common login")
            self.data = self.myDb.getInputs(self.data, mode='ask')
        if file:
            for ip in file:
                self.data["ip_address"] = ip.rstrip('\n')
                self.data = self.myDb.getInputs(self.data, mode=mode)
                self.executeCommands(self.loginTelnet(refreshing=save,privelege=privelege), command_path, silent=True)
            file.close()
        return None

    """ Common tasks"""
    def executeCommonTask(self, path):
        """execute a task from a file"""
        self.executeCommands(self.loginTelnet(privelege=True),path,silent=False)

    def createVlans(self, target, start, numberOfVlans, nameList=[] ):
        """create vlans on the taget """
        if target:
            print("Creating the vlans")
            if numberOfVlans!=0:
                text = str(start) + '-' + str(int(start)+int(numberOfVlans-1))
            else:
                text = str(start)
            self.executeLine(target, "vlan "+ text)
            self.executeLine(target, "no shutdown")
            self.executeLine(target, "exit")
            if nameList and len(nameList) == numberOfVlans:
                print("Naming the vlans")
                for i , name  in enumerate(nameList,start):
                    self.executeLine(target, "vlan "+ str(i))
                    self.executeLine(target, "name "+ str(name))
                    self.executeLine(target, "exit")
            target.close()
        return None

    def rename(self , target, name):
        """change the hostname of the device"""
        if target and name:
            print("renaming the device")
            self.executeLine(target, "hostname " + name)
            target.close()
        return None

    def saveConfig(self, target):
        """ saves the current configuration into the device"""
        pass

    """SSH part """
    """
    def loginSSH(self):
        ""connects to the device with SSh""
        try:
            if data["ip_address"]=='':
                print("Invalid ip")
                return None
            client = pk.SSHClient()
            client.load_system_host_keys()
            self.data = self.myDb.getInputs(self.data,"check")
            client.connect(self.data["ip_address"],username=self.data["username"], password=self.data["password"])
        except:
"""
