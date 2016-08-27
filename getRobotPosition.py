from naoqi import ALProxy
import time

robotIP = "nao.local"
PORT = 9559

useSensorValues = False

class RobotPosition:
    def __init__(self):
        #Creat proxy to ALMotion
        self.motionProxy = ALProxy("ALMotion", robotIP, PORT)

        #Save position in position.txt
        self.target = open("position.txt", 'a')


    def getRobotPosition(self):
        #Write down the current time extracted from robot time

        self.target.write(str(self.motionProxy.getRobotPosition(useSensorValues)))
        self.target.write("\n")

    def closeFile(self):
        self.target.close()
