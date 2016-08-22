import time
from naoqi import ALProxy


robotIP = "nao.local"
PORT = 9559

class Laser:
    def __init__(self):
        #Creat proxy to ALLaser
        self.laserProxy = ALProxy("ALLaser", robotIP, PORT)

        #Creat proxy to ALMemory
        self.memoryProxy = ALProxy("ALMemory", robotIP, PORT)

        #Set the laser ON
        self.laserProxy.laserON()

        self.target1 = open("laserCartesian.txt", 'a')

        self.target2 = open("laserPolar.txt", 'a')

    def getLaser(self):
        #Save laser data in variable laserData
        laserData = self.memoryProxy.getData("Device/Laser/Value")

        #Save Cartesian coordinations
        for item in laserData:
            self.target1.write(str(item[2]))
            self.target1.write(",")
            self.target1.write(str(item[3]))
            self.target1.write("\n")
        self.target1.write("\n")

        #Save Polar coordinations
        self.target2 = open("laserPolar.txt", 'a')
        for item in laserData:
            self.target2.write(str(item[0]))
            self.target2.write(",")
            self.target2.write(str(item[1]))
            self.target2.write("\n")
        self.target2.write("\n")

    def closeFile(self):
        
        self.laserProxy.laserOFF()
        self.target1.close()
        self.target2.close()
