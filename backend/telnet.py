import telnetlib as tn
from backend.utility import Utility
import time
import getpass


class TelnetDevice(Utility):
    """this class models a device like routers ,swithes and servers """

    def __init__(self):
        """declare the variables neeeded to specify a device """
        self.myDb = Utility()
        self.data = {'host': '', 'device_type': '', 'ip': '',
                     'port': '23', 'username': '', 'password': ''}
#""""global""""
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

#"""Telnet part"""

    def loginTelnet(self, refreshing=True, privelege=False, mode='ask'):
        """enable the user to login into the device """
        try:
            if self.data["ip"] == "":
                return None
            print("loading...")
            target = tn.Telnet()
            target.open(host=self.data['ip'], port=self.data['port'])
            self.data = self.myDb.getInputs(self.data, mode=mode)
        except (TimeoutError, OSError):
            print("Error !!! device unreacheable ")
            return None
        else:
            target.read_until("Username: ".encode())
            self.executeLine(target, self.data["username"])
            target.read_until("Password: ".encode())
            self.executeLine(target, self.data["password"])
            answer = target.read_some().decode()
            if answer.endswith(">"):
                if self.data["host"] != answer[2:-1] and refreshing:
                    self.data["host"] = answer[2:-1]
                    self.myDb.refreshSetting(self.data)
                print("Connection successful to " + self.data["ip"])
                if privelege:
                    return self.loginPrivelegeMode(target)
                return target
            else:
                print("Failed to connect to " + self.data["ip"])
                return None

    def loginPrivelegeMode(self, target):
        """login to privelege mode in a cisco device"""
        if target:
            if self.data['secret'] == '':
                self.data['secret'] = getpass.getpass(
                    "Input the enable password : ")
            self.executeLine(target, "en")
            self.executeLine(target, self.data['secret'])
            answer = target.read_some().decode()
            if answer.endswith("#"):
                print("Getting into the privelege mode")
                return target
            else:
                print("incorrect password", end=' ')
                target.close()
                return None

    def executeCommands(self, target, fromfile=True, data="backend/list_of_commands.txt", silent=True):
        """execute commands from a file into one device"""
        if fromfile:
            file = self.myDb.openFile(data)
        if target and file:
            self.executeLine(target, "terminal length 0")
            for command in file:
                self.executeLine(target, command)
            self.executeLine(target, "exit")
            if silent:
                print("All the commands are done")
            else:
                print(target.read_all().decode())
            file.close()
            target.close()
        else:
            print("Commands did not apply!!")
        return None

    def executeLine(self, target, command):
        """executes a line of command in the target"""
        target.write((command + '\n').encode())
        time.sleep(0.2)
        return target

    def configureMultipleFromRange(self, start, end, command_path="backend/list_of_commands.txt", save=False, silent=True, privelege=False, mode="one"):
        """configure a range of ips with the same configuration"""
        if mode == "one":
            print("Enter the common login")
            self.data = self.myDb.getInputs(self.data, mode='ask')
        try:
            for ip in self.myDb.generateRange(start, end):
                self.data["ip"] = ip
                self.executeCommands(self.loginTelnet(
                    refreshing=save, privelege=privelege, mode=mode), command_path, silent=silent)
        except Exception:
            print("unknown error !! ")
        return None

    def configureMultipleFromFile(self, ip_path="backend/list_of_ip.txt", command_path="backend/list_of_commands.txt", save=False, silent=True, privelege=False, mode='one'):
        """configure a range of ips retrieved from a file with the same configuration"""
        file = self.myDb.openFile(ip_path)
        if mode == 'one':
            print("Enter the common login")
            self.data = self.myDb.getInputs(self.data, mode='ask')
        if file:
            try:
                for ip in file:
                    self.data["ip"] = ip.rstrip('\n')
                    self.executeCommands(self.loginTelnet(
                        refreshing=save, privelege=privelege, mode=mode), command_path, silent=True)
                file.close()
            except Exception:
                print("unknown error !!")
        return None

#""" Common tasks"""

    def executeCommonTask(self, path):
        """execute a task from a file"""
        self.executeCommands(self.loginTelnet(
            privelege=True), path, silent=False)

    def rename(self, name):
        """change the hostname of the device"""
        if name:
            print("renaming the device")
            command = ["hostname"+str(name)]
            self.executeCommands(self.loginTelnet(
                privelege=True, mode='check'), fromfile=False, data=command, silent=False)
        return command

    def createVlans(self, start, numberOfVlans, nameList=[] ):
        """create vlans on the target""" 
        commands = []
        print("Creating the vlans")
        if numberOfVlans > 1:
            text = str(start) + '-' + str(int(start)+int(numberOfVlans-1))
        elif numberOfVlans == 1:
            text = str(start)            
        commands.append("conf  t")
        commands.append("vlan " + text)
        commands.append("exit")
        commands.append("int vlan " + text)
        commands.append("no shut")
        commands.append("exit")
        if nameList and len(nameList) == numberOfVlans:
            print("Naming the vlans")
            for i , name  in enumerate(nameList,start):
                commands.append("vlan "+ str(i))
                commands.append("name "+ str(name))
                commands.append("exit")
        self.executeCommands(self.loginTelnet(privelege=True, mode='check'), fromfile=False, data=commands, silent=True)
        return commands

    def showRun(self):
        """displays the show run"""
        command = ["show run"]
        self.executeCommands(self.loginTelnet(privelege=True, mode='check'), fromfile=False, data=command, silent=False)
        return command
        
