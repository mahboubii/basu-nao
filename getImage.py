import time
from naoqi import ALProxy

starttime = time.time()

IP = "nao.local"
PORT = 9559

# Create a proxy to ALPhotoCapture
photoCaptureProxy = ALProxy("ALPhotoCapture", IP, PORT)

#Indicating index of next image file
target = open("count.txt", 'r+')
lines = target.readlines()
count = int(lines[0])
target.seek(0)
target.truncate()
target.write(str(count + 1))
target.close()

#Exact the file name to store
topName = "imaget" + str(count)
botName = "imageb" + str(count)

photoCaptureProxy.setHalfPressEnabled(True)

#Set image attribute
photoCaptureProxy.setResolution(0)
photoCaptureProxy.setPictureFormat("jpg")
photoCaptureProxy.setCameraID(0)

#Save top picture on NAO
photoCaptureProxy.takePicture("/home/nao/recordings/cameras/", topName)


#Save bottom picture on NAO
photoCaptureProxy.setCameraID(1)
photoCaptureProxy.takePicture("/home/nao/recordings/cameras/", botName)

photoCaptureProxy.setHalfPressEnabled(False)

endtime = time.time()

target = open("logimage.txt", 'a')
target.write("Image: %s -> %s : %s \n" % (str(starttime), str(endtime), str(endtime - starttime)))
target.close()
