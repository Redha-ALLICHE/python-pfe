import netmiko
from network_db.net_database import Net_db
from backend.utility import Utility
from PyQt5 import QtCore


class SshDevice():
    """this class ensures the operations on a device"""
    done = QtCore.pyqtSignal()

    def __init__(self, device_path='network_db/devices.db', ):
        """the constructor function"""
        self.data = {"ip": '', "username": '',
                     "password": '', "secret": '', "device_type": 'cisco_ios', "timeout": 2}
        self.myDb = Utility()
        self.temp = []

    def getInputFromUser(self):
        """retrieve the information from the user about a new device and store it in the data variable """
        self.data = self.myDb.fillData(self.data)

    def show_info(self):
        """print on the screen the informations about the device """
        print(self.data)

    def loginSsh(self, refreshing=False, privelege=True):
        """login to the device"""
        try:
            if self.data["ip"] == '':
                return None
            self.temp[2].emit("###Trying to connect to " +
                              self.data["ip"]+' ###\n')
            self.temp[2].emit("Establishing the connection...\n")
            target = netmiko.ConnectHandler(ip=self.data["ip"], username=self.data["username"],
                                            password=self.data["password"], secret=self.data["secret"], device_type='cisco_ios', timeout=2)
            self.temp[2].emit("Connection successful\n")
            if refreshing:
                self.myDb.refreshDevice(self.data, temp=self.temp)
            if privelege:
                target.enable()
            return target
        except Exception as e:
            self.temp[2].emit(e)
            return None

    def executeLine(self, target, command):
        """executes a line of a command"""
        if target:
            return target.send_command(command)
        return None

    def executeLines(self, target, commands, silent=True, privelege=False, backup=False, backup_root='temp/'):
        """executes multiple commands from a list"""
        if target:
            display = ''
            if backup:
                if not backup_root.endswith("/"):
                    backup_root += '/'
                self.myDb.prepareBackup(
                    self.data["ip"], backup_root, target.send_command("show run"), temp=self.temp)
            for command in commands:
                display += self.executeLine(target, command)
            if silent:
                self.temp[2].emit("all commands are done")
            else:
                self.temp[2].emit(display)
                self.temp[2].emit("\nOperation done\n")
        else:
            self.temp[2].emit("Operation failed")
        return None

    def automate(self, ips=[], commands=[], mode='check', privelege=True, save=False, silent=False,  backup=False, backup_root="temp/", funct=None, increment=None):
        """automate with ssh"""
        marker = False
        self.temp = increment
        if mode == 'one':
            increment[1].emit("Enter the common login")
            self.data = funct(self.data, mode='ask')
        try:
            if ips:
                if backup and backup_root == 'temp/':
                    backup_root = self.myDb.mktemp(backup_root.rstrip('/'))
                    marker = True
                for ip in ips:
                    if increment:
                        increment[0].emit(ips.index(ip))
                        increment[1].emit("Working on : " + ip)
                    self.data.update({'ip': ip})
                    if mode != "one":
                        self.data.update(
                            {'username': '', 'password': '', 'secret': ''})
                    self.data = funct(self.data, mode=mode)
                    self.executeLines(self.loginSsh(
                        refreshing=save, privelege=privelege), commands, silent=silent, backup=backup, backup_root=backup_root)
                if marker:
                    self.myDb.removeTemp(backup_root)
                increment[1].emit("Configuration done ")
        except Exception as ex:
            self.temp[2].emit(str(ex))
        increment[0].emit(len(ips))
        increment[3].emit()
        return None

    def executeFromFile(self, target, path='list_of_commands.txt'):
        """executes the commands from a file"""
        file = self.myDb.openFile(path)
        commands = []
        for line in file:
            commands.append(line.strip('\n'))
        return self.executeLines(target, commands)

    def executeMultipleFromFile(self, target, mode, command_path='list_of_commands.txt',                  ip_path="list_of_ip.txt"):
        """configure a range of ips retrieved from a file with the same configuration"""
        file = self.myDb.openFile(ip_path)
        if mode == 'one':
            print("Enter the common login")
            self.data = self.myDb.getInputs(self.data, mode='ask')
        if file:
            for ip in file:
                self.data["ip"] = ip.rstrip('\n')
                self.data = self.myDb.getInputs(self.data, mode=mode)
                self.executeFromFile(self.loginSsh(), command_path)
            file.close()
            self.close(target)
        return None

    def executeMultipleFromRange(self, target, mode, start, end, command_path='list_of_commands.txt'):
        """configure a range of ips retrieved from a file with the same configuration"""
        if mode == 'one':
            print("Enter the common login")
            self.data = self.myDb.getInputs(self.data, mode='ask')
            for ip in self.myDb.generateRange(start, end):
                self.data["ip"] = ip
                self.data = self.myDb.getInputs(self.data, mode=mode)
                self.executeFromFile(self.loginSsh(), command_path)
            self.close(target)
        return None

    def close(self, target):
        """closes the connection """
        if target:
            return target.disconnect()
        return None
