import threading
import time
from backend.utility import Utility

class Background(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, ips=[], interval=1 ):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.myDb = Utility()
        self.interval = interval
        self.ips = ips

        thread = threading.Thread(target=self.task, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def pingRange(self, ipRange):
        """ping all the devices in the range"""
        x=''
        for ip in ipRange:
           
            x = self.myDb.ping(ip)
            if x:
                print("the device " + ip + " is up !!")
            else:
                print("the device " + ip + " is down !!")

    def task(self):
        """ Method that runs forever """
        while True:
            self.pingRange(self.ips)
            time.sleep(self.interval)



