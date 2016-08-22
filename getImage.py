import time
from naoqi import ALProxy

IP = "nao.local"
PORT = 9559

class Image:
    def __init__(self):
        # Create a proxy to ALPhotoCapture
        self.photoCaptureProxy = ALProxy("ALPhotoCapture", IP, PORT)

        self.photoCaptureProxy.setHalfPressEnabled(True)

        #Set image attribute
        self.photoCaptureProxy.setResolution(0)
        self.photoCaptureProxy.setPictureFormat("jpg")

    def getImage(self):

        #Indicating index of next image file
        count = open("count.txt", 'r+')
        lines = count.readlines()
        countNum = int(lines[0])
        count.seek(0)
        count.truncate()
        count.write(str(countNum + 1))
        count.close()

        #Exact the file name to store
        topName = "imaget" + str(countNum)
        botName = "imageb" + str(countNum)

        #Save top picture on NAO
        self.photoCaptureProxy.setCameraID(0)
        self.photoCaptureProxy.takePicture("/home/nao/recordings/cameras/", topName)

        #Save bottom picture on NAO
        self.photoCaptureProxy.setCameraID(1)
        self.photoCaptureProxy.takePicture("/home/nao/recordings/cameras/", botName)

    def closeFile(self):
        self.photoCaptureProxy.setHalfPressEnabled(False)
