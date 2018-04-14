import sqlite3

class Net_db():
    """ths class manages the database of the devices """
    def __init__(self, path='devices.db'):
        self.path = path
        self.keys = ["ip","hostname","device_type","username","password","secret","telnet_port"]
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()
        self.ips = self.getIps()

    def createDb(self):
        """creates the table of the database"""
        try:
            self.cur.execute(
                """CREATE TABLE DEVICES (id INTEGER PRIMARY KEY AUTOINCREMENT ,
                ip TEXT NOT NULL UNIQUE,
                hostname TEXT ,
                device_type TEXT,
                username TEXT,
                password TEXT,
                secret TEXT,
                telnet_port INTEGER)
                """)
            self.conn.commit()
        except sqlite3.OperationalError:
            print('Erreur la table existe déjà')
        except Exception:
            print("Erreur")

    def getIps(self):
        """retrieve an array of ips"""
        ips = []
        devices = self.cur.execute("SELECT * FROM DEVICES")
        if devices:
            for data in devices:
                ips.append(data[1])
        return ips

    def addDevice(self, data):
        """adds a device to the database and return the id"""
        if data["ip"] in self.ips:
            print("the ip of the device already exists")
        else:
            self.cur.execute("INSERT INTO DEVICES (ip,hostname,device_type,username,password,secret,telnet_port) VALUES (:ip,:hostname,:device_type,:username,:password,:secret,:telnet_port)", (data))
            print("A new device added!! ")
            self.ips.append(data['ip'])
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
            
def main():
    dev = Net_db()
    dev.createDb()
    dev.showDb()
    dev.addDevice({"ip":"192.168.1.1", "hostname":"enst", "device_type":"", "username":"root",
                   "password":"root", "secret":"1234", "telnet_port":23})
    #dev.showDb()
    dev.addDevice({"ip": "192.168.1.2", "hostname": "enst", "device_type": "", "username": "root",
                   "password": "root", "secret": "1234", "telnet_port": 23})
    print("**")
    dev.updateDevice({"ip": "192.168.1.3", "hostname": "farr", "device_type": "", "username": "root",
                            "password": "root", "secret": "1234", "telnet_port": 23})

    dev.showDb()
    dev.closeDb()
  
if __name__ == '__main__':
    main()
