from backend.telnet import TelnetDevice

item = TelnetDevice()
#item.configureMultipleFromRange("192.168.1.15", "192.168.1.17",privelege=True, silent=False,mode="check")
#item.createVlans(con, 2, 1)
item.configureMultipleFromRange("192.168.1.15", "192.168.1.17", privelege=True, silent=False,  save=True,mode="check")
#item.data["ip"]='192.168.1.15'
#item.rename("enst")
#item.configureMultipleFromFile(save=False, privelege=True, mode='ask')



