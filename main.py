from backend.telnet import TelnetDevice

item = TelnetDevice()
#item.automate(ips=['192.168.1.15'],commands=item.showRun(),mode='check', silent=False, backup=True)
item.configureMultipleFromRange("192.168.1.15", "192.168.1.15", command_path=item.rename("kkk"), privelege=True, silent=False, mode="check", backup=True)
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.17", command_path=['show run'], privelege=True, silent=False, mode="check", backup=False)
item.undo()
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.15", command_path=['show run'], privelege=True, silent=False, mode="check", backup=False)
#item.createVlans(con, 2, 1)
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.18", privelege=True, silent=False,  save=False,mode="check")
#item.backup(['192.168.1.15'])
#item.data["ip"]='192.168.1.16'
#item.invokeshell()
#item.createVlans(2,3)
#item.showRun()
#item.configureMultipleFromFile(save=False, silent=False , privelege=True, mode='check')
#item.restore('backups/192.168.1.15_20_04_2018_22h29.conf')
#item.undo()
