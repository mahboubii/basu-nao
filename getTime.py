import time
from naoqi import ALProxy

starttime = time.time()

robotIP = "nao.local"
PORT = 9559

# Create a proxy to DCM
dcmProxy = ALProxy("DCM",robotIP,PORT)

#Write down the current time extracted from robot time
target = open("time.txt", 'a')

target.write(str(dcmProxy.getTime(0)))
target.write("\n")

target.close()

endtime = time.time()

target = open("logtime.txt", 'a')
target.write("time: %s -> %s : %s \n" % (str(starttime), str(endtime), str(endtime - starttime)))
target.close()
