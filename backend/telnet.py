import telnetlib as tn
from backend.utility import Utility
import time
import getpass
import subprocess
import sys
from PyQt5 import QtCore

class TelnetDevice(QtCore.QObject):
    """this class models a device like routers ,swithes and servers """

    def __init__(self):
        """declare the variables neeeded to specify a device """
        super().__init__()
        self.myDb = Utility()
        self.data = {'host': '', 'device_type': '','type':'', 'ip': '','port': '23', 'username': '', 'password': '', 'secret': '','description':'','path':'device_data/'}
        self.temp = []

#""""global""""

    def getInputFromUser(self):
        """retrieve the information from the user about a new device and store it in the data variable """
        self.data = self.myDb.fillData(self.data)

    def show_info(self):
        """self.temp[2].insertPlainText on the screen the informations about the device """
        self.temp[2].insertPlainText(self.data)

    def setData(self, newData):
        """the setter of data"""
        if newData:
            self.data = newData
        else:
            return None

#"""Telnet part"""
#"""Login and executing commands"""

    def loginTelnet(self, refreshing=True, privelege=False, mode='ask'):
        """enable the user to login into the device """
        try:
            if self.data["ip"] == "":
                return None
            target = tn.Telnet()
            self.temp[2].insertPlainText("Trying to connect to " + self.data["ip"]+'\n')
            target.open(host=self.data['ip'])
            self.temp[2].insertPlainText("Establishing the connection...\n")
        except (TimeoutError, OSError):
            self.temp[2].insertPlainText("Error !!! device unreacheable \n")
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
                    self.myDb.refreshDevice(self.data)
                self.temp[2].insertPlainText("Connection successful to " + self.data["ip"] + "\n")
                if privelege:
                    return self.loginPrivelegeMode(target)
                return target
            else:
                self.temp[2].insertPlainText("Failed to connect to " + self.data["ip"] + "\n")
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
                self.temp[2].insertPlainText("Getting into the privelege mode\n")
                return target
            else:
                self.temp[2].insertPlainText("incorrect password\n")
                target.close()
                return None

    def executeCommands(self, target, commands=[], silent=True, backup=False, backup_root='temp/'):
        """execute commands from a list of commands into one device"""
        if target and commands:
            self.executeLine(target, "terminal length 0")
            if backup:
                self.executeLine(target, "show run")
                target.read_until('#'.encode())
                self.myDb.prepareBackup(self.data["ip"], backup_root, target.read_until('#'.encode()).decode())
            for command in commands:
                QtCore.QCoreApplication.processEvents()
                self.executeLine(target, command)
            self.executeLine(target, "exit")
            if silent:
                self.temp[2].insertPlainText("All the commands are done\n")
            else:
                self.temp[2].insertPlainText(target.read_all().decode()+"\n")
            target.close()
        else:
            self.temp[2].insertPlainText("Commands did not apply!!\n")
        return None

    def executeLine(self, target, command):
        """executes a line of command in the target"""
        target.write((command + '\n').encode())
        time.sleep(0.2)
        return target

#"""automate the configuration """

    def configureMultipleFromRange(self, start, end, command_path="backend/list_of_commands.txt", save=False, silent=True, privelege=False, mode="one",backup=False):
        """configure a range of ips with the same configuration"""
        commands = command_path
        if type(command_path)==str:
            commands = self.myDb.getList(command_path)
        ips = self.myDb.generateRange(start, end)
        self.automate(ips, commands, mode=mode, privelege=privelege, save=save, silent=silent, backup=backup)
        return None

    def configureMultipleFromFile(self, ip_path="backend/list_of_ip.txt", command_path="backend/list_of_commands.txt", save=False, silent=True, privelege=False, mode='ask', backup=False):
        """configure a range of ips retrieved from a file with the same configuration"""
        commands = command_path
        if type(command_path) == str:
            commands = self.myDb.getList(command_path)
        ips = self.myDb.getList(ip_path)
        self.temp[2].insertPlainText(commands)
        self.automate(ips, commands, mode=mode, privelege=privelege, save=save, silent=silent, backup=backup)
        return None

    def automate(self, ips=[], commands=[], mode='check', privelege=True, save=False, silent=True, backup=False, backup_root='temp/', increment=None , funct=None):
        """apply a list of commands into a list of ips """
        marker = False
        self.temp = increment
        if mode == 'one':
            increment[1].setText("Enter the common login")
            self.data = funct(self.data, mode='ask')
        try:
            if ips and commands:
                if backup and backup_root=='temp/':
                    backup_root = self.myDb.mktemp(backup_root.rstrip('/'))
                    marker = True
                for ip in ips:
                    QtCore.QCoreApplication.processEvents()
                    if increment:
                        increment[0].setValue(increment[0].value() + 1)
                        increment[1].setText("Working on : " + ip )
                    self.data.update({'host': '', 'device_type': '', 'ip': ip,
                                      'port': '23', 'username': '', 'password': '', 'secret': ''})
                    self.data = funct(self.data, mode=mode)
                    self.executeCommands(self.loginTelnet(
                        refreshing=save, privelege=privelege, mode=mode), commands, silent=silent, backup=backup, backup_root=backup_root)
                if marker:
                    self.myDb.removeTemp(backup_root)
                increment[1].setText("Configuration done ")
        except Exception as ex:
            self.temp[2].insertPlainText(str(ex))
        return None

#""" Common tasks"""
    def invokeshell(self):
        """invoke a putty telnet shell"""
        if sys.platform.startswith('win'):
            puttypath = 'putty.exe'
            subprocess.call([puttypath, '-telnet', self.data["ip"]],
                            creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.call(["plink", "-telnet", self.data["ip"]])
            
    def executeCommonTask(self, path):
        """execute a task from a file"""
        self.executeCommands(self.loginTelnet(
            privelege=True), path, silent=False)

    def rename(self, name):
        """change the hostname of the device"""
        if name:
            self.temp[2].insertPlainText("renaming the device")
            command = ["conf t", "hostname "+str(name), "exit "]
        return command

    def createVlans(self, start, numberOfVlans, nameList=[]):
        """create vlans on the target"""
        commands = []
        self.temp[2].insertPlainText("Creating the vlans\n")
        if numberOfVlans > 1:
            text = str(start) + '-' + str(int(start)+int(numberOfVlans-1))
        elif numberOfVlans == 1:
            text = str(start)
        commands.append("conf  t")
        commands.append("vlan " + text)
        commands.append("exit")
        if nameList and len(nameList) == numberOfVlans:
            self.temp[2].insertPlainText("Naming the vlans\n")
            for i, name in enumerate(nameList, start):
                commands.append("vlan " + str(i))
                commands.append("name " + str(name))
                commands.append("exit")
        commands.append("exit")
        return commands

    def showRun(self):
        """displays the show run"""
        command = ["show run"]
        return command

    def backup(self, ips, root_path='backups/'):
        """get the config from a device and store it to a file"""
        self.automate(ips, [' '],mode='check', backup=True, backup_root=root_path)
        return None

    def mergeConfig(self, config_path, ips=''):
        """apply the configuration from a file to one or many devices"""
        ip = ips
        if ip == '':
            ip = [config_path.split('_')[0].split('/')[-1]]
        with open(config_path) as f:
            data = f.read(5000)
        self.automate(ips=ip, commands=['conf t', str(data)], backup=False, silent=False)
        self.temp[2].insertPlainText("restoring from : " + config_path + "and merging with the actual config")

    def save(self):
        """return the commands for saving configs"""
        return ['copy running-config startup-config', ' ']

    def restore(self, config_path, ips=''):
        """apply the configuration from a file to one or many devices"""
        ip = ips
        if ip=='':
            ip = [config_path.split('_')[0].split('/')[-1]]
        with open(config_path) as f:
            old_config = f.read(5000)
        for addr in ip:
            self.data.update({'host': '', 'device_type': '', 'ip': addr,'port': '23', 'username': '', 'password': '', 'secret': ''})
            target = self.loginTelnet(privelege=True, mode='check')
            if target:
                self.executeLine(target, "terminal length 0")
                self.executeLine(target, "show run")
                target.read_until('#'.encode())
                actual_config = target.read_until('#'.encode()).decode().split("\n")[3:-2]
                new_config = self.myDb.getRestore(actual_config, old_config)
                self.executeLine(target, "conf t")
                self.executeLine(target, str(new_config + '\n'))
                self.executeLine(target, "exit")
                target.close()
            else:
                self.temp[2].insertPlainText("Commands did not apply!!")
            self.temp[2].insertPlainText("restoring " + "from : " + config_path)
        return None

    def undo(self):
        """undo the previous configuration"""
        path = 'temp/'
        files = self.myDb.getfiles(path)
        for file in files:
            path = 'temp/'+ str(file)
            self.restore(path)

    def enableSsh(self, ips, domain_name):
        """enables the ssh protocol on the target for remote connection"""
        if len(domain_name) == len(ips):
            for i,ip in enumerate(ips):
                self.automate(ips=[ip], commands=['conf t','ip domain-name '+ domain_name[i], 'crypto key generate rsa modulus 1024','line vty 0 4','transport input all','exit'], backup=True, silent=True,save=True)
            self.temp[2].insertPlainText("setting up the ssh")
        else:
            self.temp[2].insertPlainText("No matching lengh between input")
