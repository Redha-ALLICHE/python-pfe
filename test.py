from backend.device1 import Device

device = Device()
device.getInputFromUser()
con = device.connect()
print(device.executeLine(con, "show version"))
device.close(con)