import naoqi
from naoqi import ALProxy

robotIP = "nao.local"
PORT = 9559

# Create a proxy to DCM
dcmProxy = ALProxy("DCM",robotIP,PORT)

#Write down the current time extracted from robot time
target = open("time.txt", 'a')

target.write(str(dcmProxy.getTime(0)))
target.write("\n")

target.close()
