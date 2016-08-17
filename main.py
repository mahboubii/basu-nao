import os
import sys
import time
import argparse
import almath
from naoqi import ALProxy

def checkIfLaserChanged(oldData, laserProxy, memoryProxy):
    #Set the laser ON
    laserProxy.laserON()

    # Get new laser data
    laserData = memoryProxy.getData("Device/Laser/Value")

    # check if laser data has changed
    if(laserData != oldData):
        return [laserData , 0]
    else:
        return [laserData , 1]

def main(robotIP, PORT = 9559):

    time.sleep(10)

    # Create proxy to ALBasicAwareness
    basic_awareness = ALProxy("ALBasicAwareness",robotIP, PORT)

    # Create proxy to ALVideoRecorder
    videoRecorderProxy = ALProxy("ALVideoRecorder", robotIP, PORT)

    # Create proxy to ALMotion
    motionProxy = ALProxy("ALMotion", robotIP , PORT)

    #Creat proxy to ALLaser
    laserProxy = ALProxy("ALLaser", robotIP, PORT)

    #Creat proxy to ALMemory
    memoryProxy = ALProxy("ALMemory", robotIP, PORT)

    # Wake up the Robot
    motionProxy.wakeUp()
    motionProxy.moveInit()

    # Stop awareness and lock the head
    basic_awareness.stopAwareness()
    motionProxy.setStiffnesses("Head", 1.0)

    # Setting the straight in the horizon
    names      = ["HeadYaw", "HeadPitch"]
    angleLists = [0.0*almath.TO_RAD, 0.0*almath.TO_RAD]
    timeLists  = [0.5, 0.5]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    #Start recording
    videoRecorderProxy.setResolution(2)
    videoRecorderProxy.startRecording("/home/nao/recordings/cameras", "test")

    laserValue = [0 , 0]

    start = time.time()

    #Move forward for 1 min
    motionProxy.moveToward(0.7, 0.0, -0.05)

    #Get data every 1 sec till the end of move
    while ((time.time() - start) < 60):
        #while(laserValue[1] and ((time.time() - start) < 60)):
        #    laserValue = checkIfLaserChanged(laserValue[0] ,laserProxy ,memoryProxy)
        os.system("sh getData.sh")
        laserValue[1] = 1
        print "raft"
        time.sleep(1)

    motionProxy.stopMove()

    #stop recording
    videoRecorderProxy.stopRecording()

    basic_awareness.startAwareness()

    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
