import time
from naoqi import ALProxy

starttime = time.time()


robotIP = "nao.local"
PORT = 9559

#Creat proxy to ALLaser
laserProxy = ALProxy("ALLaser", robotIP, PORT)

#Creat proxy to ALMemory
memoryProxy = ALProxy("ALMemory", robotIP, PORT)

#Set the laser ON
laserProxy.laserON()

#Save laser data in variable laserData
laserData = memoryProxy.getData("Device/Laser/Value")

#Save Cartesian coordinations
target = open("laserCartesian.txt", 'a')
for item in laserData:
    target.write(str(item[2]))
    target.write(",")
    target.write(str(item[3]))
    target.write("\n")
target.write("\n")
target.close()

#Save Polar coordinations
target = open("laserPolar.txt", 'a')
for item in laserData:
    target.write(str(item[0]))
    target.write(",")
    target.write(str(item[1]))
    target.write("\n")
target.write("\n")
target.close()

endtime = time.time()

target = open("logLaser.txt", 'a')
target.write("Laser: %s -> %s : %s \n" % (str(starttime), str(endtime), str(endtime - starttime)))
target.close()
