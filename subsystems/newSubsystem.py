import wpilib
import commands2
import rev
import phoenix6
import phoenix5
import logging

logger = logging.getLogger("Vision")

from constants import SW, ELEC

class NewSubsystemClass(commands2.Subsystem):
    def __init__(self) -> None:
        # Inside of the init method you will declare any motors, sensors, vraiables, and booleans
        # You can also define a variable to a specific class from a library you may have imported
        
        # Initialize phoenix motor
        self.phoenixMotor = phoenix6.hardware.TalonFX(1)
        
        # Control Objects (Still working on them)
        self.back = phoenix6.controls.VelocityDutyCycle(1, 1, True, -.2)
        self.forward = phoenix6.controls.VelocityDutyCycle(1, 1, True, .2, 0, False, False, False)
        self.stop = phoenix6.controls.VelocityDutyCycle(1, 1, True, 0, 0, False, False, False)
    
    # motorGroupForward method will set both motors 1 & 2 forward using the motorGroup variable
    def motorGroupForward(self):
        self.phoenixMotor.set_control(self.forward)
        
    # motorGroupBackward method will set both motors 1 & 2 backwards using the motorGroup variable
    def motorGroupBackward(self):
        self.phoenixMotor.set_control(self.back)
        
    # stopMotors methhod will stop both motors
    def stopMotors(self):
        self.phoenixMotor.set_control(self.stop)
        
    # these methods will only run if they are called/summoned in by a command in the commands folder