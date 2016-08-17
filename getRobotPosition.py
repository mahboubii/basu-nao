from naoqi import ALProxy
import time

robotIP = "nao.local"
PORT = 9559

starttime = time.time()

#Creat proxy to ALMotion
motionProxy = ALProxy("ALMotion", robotIP, PORT)

#Save position in position.txt
target = open("position.txt", 'a')
useSensorValues = True

target.write(str(motionProxy.getRobotPosition(useSensorValues)))
target.write("\n")

target.close()

endtime = time.time()

target = open("logPose.txt", 'a')
target.write("robot position: %s -> %s : %s \n" % (str(starttime), str(endtime), str(endtime - starttime)))
target.close()
