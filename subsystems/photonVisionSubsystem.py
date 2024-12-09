import wpilib
import commands2
import photonlibpy
import logging
import wpinet

logger = logging.getLogger("Vision")

from photonlibpy import estimatedRobotPose
from photonlibpy import multiTargetPNPResult
from photonlibpy.photonCamera import PhotonCamera
from photonlibpy.photonPipelineResult import PhotonPipelineResult
from photonlibpy import packet
from photonlibpy import photonPoseEstimator
from photonlibpy.photonTrackedTarget import PhotonTrackedTarget

from wpimath.geometry import Pose3d, Transform3d, Translation3d
from wpimath.units import metersToFeet, metersToInches

from wpilib import SmartDashboard, Field2d

from constants import OP

class visionSubsystem(commands2.Subsystem):
    
    def __init__(self) -> None:
        
        # Define camera
        self.camera = PhotonCamera("AprilTagCam")
        
        # gets latest result from camera
        self.result = self.camera.getLatestResult()
        
        # Checks if camera detects targets
        self.hasTargets = self.result.hasTargets()
        
        # Recieves the latest targets seen by the camera
        self.targets = self.result.getTargets()
        
        # April Tag Layout   (Currently empty/ not being used)
        self.pose = photonPoseEstimator
        
        # # Position estimation strategy that is used by the PhotonPoseEstimator class   (Currently empty/ not being used)
        self.PoseStrat = photonPoseEstimator.PoseStrategy.CLOSEST_TO_REFERENCE_POSE
        
        # Booleans used for vision
        self.targetVisible = False
        
        wpinet.PortForwarder.getInstance().add(5810, "photonvision.local", 5800) # Untested

        
    # def getTargetID(self, id: int): # Return a list of tags beeing seen (untested)
    #     """
    #     Returns all the aprilTag id's it currently sees.
    #     """
    #     results = self.targets
    #     if len(results) > 0:
    #         for i in results:
    #             if results[-1].getFiducialId() > id:
    #             # return results[-2].getFiducialId()
    #     else:
    #         return 0
  
    def getTragetData(self, id: int, dataType: str) -> float: # Simpler version to get target data (Trying to fix)
        """
        Returns desired aprilTag data. If desired april tag is not seen by camera, default returned value is 0.
        
        :param ID:       The aprilTag ID you want to get data from.
        :param dataType: The type of data you want returned. Current data it can retrun: `Yaw`, `Pitch`, `Skew`, `Area`, `X-Dist`, `Y-Dist`, `Z-Dist`.
        """
        
        result = self.targets
        if len(result) > 0: # Checks to see if any AprilTags are seen
            # result = result[-1] # Get most recent data
            for target in self.targets:
                if target.getFiducialId() == id: # looks for desired AprilTag ID
                    self.targetVisible = True
                    # Return the desired type of data
                    if dataType == "Yaw":
                        Data = target.getYaw()
                    elif dataType == "Pitch":
                        Data = target.getPitch()
                    elif dataType == "Skew":
                        Data = target.getSkew()
                    elif dataType == "Area":
                        Data = target.getArea()
                    elif dataType == "X-Dist":
                        Data = target.getBestCameraToTarget().X()
                    elif dataType == "Y-Dist":
                        Data = target.getBestCameraToTarget().Y()
                    elif dataType == "Z-Dist":
                        Data = target.getBestCameraToTarget().Z()
                else:
                    return 0
        else:
            return 0
        return Data
    
    def periodic(self) -> None:
        
        # Update Vision Data
        self.result = self.camera.getLatestResult()
        self.hasTargets = self.result.hasTargets()
        self.targets = self.result.getTargets()
        
        # # Using this to test the getTargetData method
        # logger.info(f"{self.getTragetData(4, "X-Dist")} data value")
        # logger.info(f"{len(self.targets)} target amount?")