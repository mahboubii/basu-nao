from naoqi import ALProxy

robotIP = "nao.local"
PORT = 9559

#Creat proxy to ALMotion
motionProxy = ALProxy("ALMotion", robotIP, PORT)

#Save position in position.txt
target = open("position.txt", 'a')
useSensorValues = True

target.write(str(motionProxy.getRobotPosition(useSensorValues)))
target.write("\n")

target.close()
