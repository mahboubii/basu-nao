import threading
from getTime import Time
from getImage import Image
from getLaser import Laser
from getSonar import Sonar
from getRobotPosition import RobotPosition
from getHeadPose import HeadPose

class Data:

    def __init__(self):
        # Create a proxy to DCM
        self.time = Time()
        self.image = Image()
        self.laser = Laser()
        self.sonar = Sonar()
        self.pose = RobotPosition()
        self.headPose = HeadPose()

    def getData(self):

        threading.Thread(target=self.time.getTime).start()
        threading.Thread(target=self.image.getImage).start()
        threading.Thread(target=self.laser.getLaser).start()
        threading.Thread(target=self.sonar.getSonar).start()
        threading.Thread(target=self.pose.getRobotPosition).start()
        threading.Thread(target=self.headPose.getHeadPose).start()

    def closeFiles(self):

        self.time.closeFile()
        self.image.closeFile()
        self.laser.closeFile()
        self.sonar.closeFile()
        self.pose.closeFile()
        self.headPose.closeFile()
