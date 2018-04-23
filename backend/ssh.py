import netmiko
from network_db.net_database import Net_db
from utility import Utility

class Device():
    """this class ensures the operations on a device"""

    def __init__(self, device_path='network_db/devices.db', ):
        """the constructor function"""
        self.device = {"ip": '', "hostname": '', "username": '',
                       "password": '', "secret": '', "port": '23', "device_type": ''}
        self.myDb = Utility()

    def getInputFromUser(self):
        """retrieve the information from the user about a new device and store it in the data variable """
        self.data = self.myDb.fillData(self.data)

    def show_info(self):
        """print on the screen the informations about the device """
        print(self.data)

    def storeToDb(self):
        """stores the local device into the database"""
        self.myDb.refreshDevice(self.device)

    def connect(self):
        """login to the device"""
        if self.device["ip"] == '':
            return None
        return netmiko.ConnectHandler(**self.device).session_preparation()

    def executeLine(self, target, command):
        """executes a line of a command"""
        if target:
            return target.send_command(command)
        return None

    def executeLines(self, target, commands):
        """executes multiple commands from a list"""
        if target:
            return target.send_config_set(commands)
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
                self.executeFromFile(self.connect(), command_path)
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
                self.executeFromFile(self.connect(), command_path)
            self.close(target)
        return None

    def close(self, target):
        """closes the connection """
        if target:
            return target.disconnect()
        return None
