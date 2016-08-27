from naoqi import ALProxy
import time

robotIP = "nao.local"
PORT = 9559

name = "CameraTop"
useSensorValues = False

class HeadPose:
    def __init__(self):
        #Creat proxy to ALMotion
        self.motionProxy = ALProxy("ALMotion", robotIP, PORT)

        #Save position in position.txt
        self.target = open("HeadPose.txt", 'a')


    def getHeadPose(self):
        #Write down the current time extracted from robot time
        frame = 0
        self.target.write(str(self.motionProxy.getPosition(name, frame, useSensorValues)))
        self.target.write("\n")

        frame = 1
        self.target.write(str(self.motionProxy.getPosition(name, frame, useSensorValues)))
        self.target.write("\n")

        frame = 2
        self.target.write(str(self.motionProxy.getPosition(name, frame, useSensorValues)))
        self.target.write("\n")

        self.target.write("\n")


    def closeFile(self):
        self.target.close()
