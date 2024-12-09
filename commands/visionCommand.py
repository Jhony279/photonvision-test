import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from subsystems.photonVisionSubsystem import visionSubsystem

import constants

import logging
logger = logging.getLogger("VisionSubsystem")

class displayingData(commands2.Command):
    def __init__(self, visionSub: visionSubsystem):
        super().__init__()
        self.VisionSub = visionSub
        
    def initialize(self):
        logger.info("Showing april tag 12 data")
        
    def execute(self):
        value = self.VisionSub.getTragetData(12, "Yaw")
        logger.info(f"Yaw Value {value}")

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        logger.info("command end")
        
class displaySeenAprilTags(commands2.Command):
    def __init__(self, visionSub: visionSubsystem):
        super().__init__()
        self.VisionSub = visionSub
        
    def initialize(self):
        logger.info("Showing all aprilTags")
        
    def execute(self):
        logger.info(f"ID: {self.VisionSub.getTargetID(12)}")

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        logger.info("command end")