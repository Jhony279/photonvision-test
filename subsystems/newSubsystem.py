import wpilib
import commands2
import phoenix6
import logging
import wpimath.controller

logger = logging.getLogger("Vision")

from constants import SW, ELEC

class NewSubsystemClass(commands2.Subsystem):
    def __init__(self) -> None:
        # Inside of the init method you will declare any motors, sensors, vraiables, and booleans
        # You can also define a variable to a specific class from a library you may have imported
        
        # Initialize phoenix motor
        self.phoenixMotor = phoenix6.hardware.TalonFX(1)
        
        # Control Objects (Still working on them)
        self.back = phoenix6.controls.VelocityDutyCycle(0, 0, True, -.2)
        self.forward = phoenix6.controls.VelocityDutyCycle(0, 0, True, .2)
        self.stop = phoenix6.controls.VelocityDutyCycle(0)
        
        # PID Controls (for fun)
        self.armPID = wpimath.controller.PIDController(.025, 0, 0)
        self.armPID.setTolerance(1)
        
        # Karken encoder (Dosent work yet)
        self.encoderVal = self.phoenixMotor.get_differential_average_position()
    
    # motorGroupForward method will set both motors 1 & 2 forward using the motorGroup variable
    def motorGroupForward(self):
        self.phoenixMotor.set_control(self.forward)
        # self.phoenixMotor.set_control(self.armPID.calculate(self.encoderVal, -115.0))
        
    # motorGroupBackward method will set both motors 1 & 2 backwards using the motorGroup variable
    def motorGroupBackward(self):
        self.phoenixMotor.set_control(self.back)
        # self.phoenixMotor.set_control(self.armPID.calculate(self.encoderVal, -115.0))
        
    # stopMotors methhod will stop both motors
    def stopMotors(self):
        self.phoenixMotor.set_control(self.stop)