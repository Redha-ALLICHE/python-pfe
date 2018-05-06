import sqlite3

class Net_db():
    """ths class manages the database of the devices """
    def __init__(self, path='network_db/devices.db'):
        self.path = path
        self.keys = ["ip","host","username","password","secret","port","device_type","type","description","path"]
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()
        try:
            self.ips = self.getIps()
        except :
            self.createDb()
            self.ips = self.getIps()

    def __len__(self):
        return len(self.ips)

    def createDb(self):
        """creates the table of the database"""
        try:
            self.cur.execute(
                """CREATE TABLE DEVICES (id INTEGER PRIMARY KEY AUTOINCREMENT ,
                ip TEXT NOT NULL UNIQUE,
                device_type TEXT,
                host TEXT ,
                type TEXT,
                username TEXT,
                password TEXT,
                secret TEXT,
                port INTEGER,
                description TEXT,
                path TEXT)
                """)
            self.conn.commit()
        except sqlite3.OperationalError:
            print('Erreur la table existe déjà')
        except Exception:
            print("Erreur")

    def getIps(self):
        """retrieve an array of ips"""
        ips = set()
        devices = self.cur.execute("SELECT * FROM DEVICES")
        if devices:
            for data in devices:
                ips.add(data[1])
        return ips

    def addDevice(self, data, overwrite='False'):
        """adds a device to the database and return the id"""
        if data["ip"] in self.ips:
            print("the ip of the device already exists")
            if overwrite:
                self.updateDevice(data)
                print("overwriting")
        else:
            self.cur.execute(
                "INSERT INTO DEVICES (ip,host,username,password,secret,port,device_type,type,description,path) VALUES (:ip,:host,:username,:password,:secret,:port,:device_type,:type,:description,:type", (data))
            print("A new device added!! ")
            self.ips.add(data['ip'])
        return self.cur.lastrowid
    
    def closeDb(self):
        """close the database"""
        self.conn.close()

    def saveDb(self):
        """saves the current changes of the device"""
        self.conn.commit()

    def deleteDevice(self, ip):
        """delete the device from the database"""
        if ip in self.ips:
            self.cur.execute("DELETE FROM DEVICES WHERE ip = (?)",(ip,))
            print("deleting the ip = " + ip)
            self.ips.remove(ip)
        else:
            print("the ip doesn't exist")

    def getAll(self):
        """get all the stored data in the database"""
        data = []
        device = {}
        temp = self.cur.execute("SELECT * FROM DEVICES").fetchall()
        if temp:
            for item in temp:
                for i, field in enumerate(self.keys):
                    device[field] = item[i+1]
                data.append(device.copy())
        return data

    def getDevice(self, ip):
        """return a dectionnary of the information about the device"""
        data = {}
        if ip in self.ips:
            temp = self.cur.execute("SELECT * FROM DEVICES WHERE ip = ?", (ip,)).fetchone()
            for i, item in enumerate(self.keys):
                data[item]=temp[i+1]
            return data           
        else:
            print("didn't find the ip in the database")
            return None

    def updateDevice(self, data):
        """update the information about the device"""
        old = self.getDevice(data["ip"])
        if old:
            for info in self.keys:
                if data[info] != old[info] and info != 'ip':
                    self.cur.execute("UPDATE DEVICES SET {} = ? WHERE ip = ?".format(info),(data[info],data["ip"]))
        else:
            self.addDevice(data)

    def showDb(self):
        self.cur.execute("""SELECT * FROM DEVICES""")
        for row in self.cur:
            print(row)

            
""" def main():
    dev = Net_db()
    dev.createDb()
    dev.showDb()
    dev.addDevice({"ip":"192.168.1.1", "host":"enst", "device_type":"", "username":"root",
                   "password":"root", "secret":"1234", "port":23})
    #dev.showDb()
    dev.addDevice({"ip": "192.168.1.2", "host": "enst", "device_type": "", "username": "root",
                   "password": "root", "secret": "1234", "port": 23})
    print("**")
    dev.updateDevice({"ip": "192.168.1.3", "host": "farr", "device_type": "", "username": "root",
                            "password": "root", "secret": "1234", "port": 23})
    print(dev.getDevice("192.168.1.1"))
    print(dev.getAll())
    dev.closeDb()
  

if __name__ == '__main__':
    main()
 """