import time
from naoqi import ALProxy

robotIP = "nao.local"
PORT = 9559

RVal = "Device/SubDeviceList/US/Right/Sensor/Value"
LVal = "Device/SubDeviceList/US/Left/Sensor/Value"

class Sonar:
    def __init__(self):
       # Create proxy to ALMemory
       self.memoryProxy = ALProxy("ALMemory", robotIP, PORT)

       # Create proxy to ALSonar
       self.sonarProxy = ALProxy("ALSonar", robotIP, PORT)

       self.target = open("time.txt", 'a')

       # Turning sensor ON
       self.sonarProxy.subscribe("myApplication")


       self.target1 = open("rightSonar.txt", 'a')

       self.target2 = open("leftSonar.txt", 'a')


    def getSonar(self):

        #Save right sonar data
        self.target1.write(str(self.memoryProxy.getData(RVal)))
        self.target1.write("\n")
        for i in range(1,10):
            self.target1.write(str(self.memoryProxy.getData(RVal + str(i))))
        self.target1.write("\n")
        self.target1.write("\n")

        #Save left sonar data
        self.target2.write(str(self.memoryProxy.getData(LVal)))
        self.target2.write("\n")
        for i in range(1,10):
            self.target2.write(str(self.memoryProxy.getData(LVal + str(i))))
            self.target2.write("\n")
        self.target2.write("\n")


    def closeFile(self):
        self.target1.close()
        self.target2.close()
        # Turning sensor OFF
        self.sonarProxy.unsubscribe("myApplication")
