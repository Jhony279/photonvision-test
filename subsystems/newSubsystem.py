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
        
        # Sets variable Motor1 & motor2 to be a CANSparkMax with motor ID's 0 & 1 and define them as brushless motors
        self.revMotor1 = rev.CANSparkMax(ELEC.motor_1, rev.CANSparkMax.MotorType.kBrushless)
        self.revMotor2 = rev.CANSparkMax(ELEC.motor_2, rev.CANSparkMax.MotorType.kBrushless)
        
        self.motorGroup = phoenix6.hardware.TalonFX(1)
        
        self.back = phoenix6.controls.VelocityDutyCycle(1, 1, True, -.2)
        self.forward = phoenix6.controls.VelocityDutyCycle(1, 1, True, .2, 0, False, False, False)
        self.stop = phoenix6.controls.VelocityDutyCycle(1, 1, True, 0, 0, False, False, False)
        
        # Creates a motor group using motor1 & motor2 with the MotorControllerGroup class in the wpilib library
        # Motor groups make it easier to control multiple motors at the same time 
        
        # self.motorGroup = wpilib.MotorControllerGroup(self.revMotor1, self.revMotor2)
    
    
    # motorGroupForward method will set both motors 1 & 2 forward using the motorGroup variable
    def motorGroupForward(self):
        self.motorGroup.set_control(self.forward)
        
    # motorGroupBackward method will set both motors 1 & 2 backwards using the motorGroup variable
    def motorGroupBackward(self):
        self.motorGroup.set_control(self.back)
        
    # stopMotors methhod will stop both motors
    def stopMotors(self):
        self.motorGroup.set_control(self.stop)
        
    
    # these methods will only run if they are called/summoned in by a command in the commands folder