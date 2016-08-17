from naoqi import ALProxy

robotIP = "nao.local"
PORT = 9559

# Create proxy to ALMemory
memoryProxy = ALProxy("ALMemory", robotIP, PORT)

# Create proxy to ALSonar
sonarProxy = ALProxy("ALSonar", robotIP, PORT)

RVal = "Device/SubDeviceList/US/Right/Sensor/Value"
LVal = "Device/SubDeviceList/US/Left/Sensor/Value"

# Turning sensor ON
sonarProxy.subscribe("myApplication")

#Save right sonar data
target = open("rightSonar.txt", 'a')
target.write(str(memoryProxy.getData(RVal)))
target.write("\n")
for i in range(1,10):
    target.write(str(memoryProxy.getData(RVal + str(i))))
    target.write("\n")
target.write("\n")
target.close()

#Save left sonar data
target = open("leftSonar.txt", 'a')
target.write(str(memoryProxy.getData(LVal)))
target.write("\n")
for i in range(1,10):
    target.write(str(memoryProxy.getData(LVal + str(i))))
    target.write("\n")
target.write("\n")
target.close()

# Turning sensor OFF
sonarProxy.unsubscribe("myApplication")
