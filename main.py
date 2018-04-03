from device import Device

item = Device()
item.configureMultipleFromRange("192.168.1.15", "192.168.1.19",privelege=True,mode="check")
#item.configureMultipleFromFile(save=False, privelege=True, mode='ask')



