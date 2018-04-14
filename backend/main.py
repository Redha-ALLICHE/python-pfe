from device import Device

item = Device()
item.configureMultipleFromRange("192.168.1.15", "192.168.1.17",privelege=True, silent=False,mode="check")
#item.createVlans(con, 2, 1)
con = item.configureMultipleFromRange(
    "192.168.1.15", "192.168.1.17", privelege=True, silent=False, mode="check")
#item.configureMultipleFromFile(save=False, privelege=True, mode='ask')



