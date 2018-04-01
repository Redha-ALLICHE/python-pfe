from device import Device

item = Device()
item.setData(item.myDb.getItemByName("R2"))
item.executeCommands(item.login())



