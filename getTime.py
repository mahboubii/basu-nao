import time
from naoqi import ALProxy

robotIP = "nao.local"
PORT = 9559

class Time:
    def __init__(self):

        # Create a proxy to DCM
        self.dcmProxy = ALProxy("DCM",robotIP,PORT)
        self.target = open("time.txt", 'a')

    def getTime(self):

        #Write down the current time extracted from robot time
        self.target.write(str(self.dcmProxy.getTime(0)))
        self.target.write("\n")

    def closeFile(self):
        self.target.close()
