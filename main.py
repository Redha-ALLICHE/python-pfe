from backend.telnet import TelnetDevice
from backend.ssh import SshDevice
from backend.background import Background

item = SshDevice()
#item.automate(ips=['192.168.1.15'],commands=item.showRun(),mode='check', silent=False, backup=True)
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.15", command_path=item.rename("kkk"), privelege=True, silent=False, mode="check", backup=True)
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.17", command_path=['show run'], privelege=True, silent=False, save=True,mode="check", backup=False)
#item.undo()
"""base = Background(['192.168.1.15'])
import time 
time.sleep(25)
print("rer")"""
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.16", command_path=['show run'], privelege=True, silent=False, mode="check", backup=False)
#item.createVlans(con, 2, 1)
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.18", privelege=True, silent=False,  save=False,mode="check")
#item.backup(['192.168.1.15'])
item.data["ip"]='192.168.1.16'
item.data["username"]="root"
item.data["password"]="1234"
item.data["secret"]="124"
item.data["device_type"]="cisco_ios"
item.loginSsh()
#item.invokeshell()
#item.createVlans(2,3)
#item.showRun()
#item.configureMultipleFromFile(save=False, silent=False , privelege=True, mode='check')
#item.restore('backups/192.168.1.15_20_04_2018_22h29.conf')
#item.undo()
#item.enableSsh(['192.168.1.17'],['enst.dz'])
