import wpilib
import commands2
import commands2.cmd

# everytime you make a new command file you will have to import the class for the subsytem this command is for
# Since this command is for newSubsystem I will import the class that is inside the newSubsystem file and in this case it is called NewSubsystemClass
from subsystems.newSubsystem import NewSubsystemClass

# Logging is useful if you wanna display info onto the driverstation
import logging
logger = logging.getLogger("NewSubsystem")

class MotorForwardCommand(commands2.Command):
    
    # Inside the parameters of init im assigning the variable newSubsystem to the class that is inside the newSubsystem file called NewSubsystemClass
    # You can assign multiple subsystem classes inside the init parameters if the command is meant to control more than one subsystem
    def __init__(self, newSubsystem: NewSubsystemClass):
        super().__init__()
        
        # Assigns newSub to the class newSubsystem
        self.newSub = newSubsystem 
        
        # This method makes the newSubsytem a rquirement for the command to be able to run and prevents it from being used by another command at the same time
        self.addRequirements(newSubsystem)
        
    # Anything inside this method will only run once at the very beggining of when the command is called/summoned
    def initialize(self):
        logger.info("Motors Forward")
        
    # Anything inside this method will run/will be updated 50 times a second
    def execute(self):
        self.newSub.motorGroupForward()
        
    # This method will end the entire command if the returned boolean is true
    def isFinished(self) -> bool:
        return False
    
    # Anything in this method will only run once when the command is ending
    def end(self, interrupted: bool):
        self.newSub.stopMotors()
        
# Anytime you are creating a new command you have to create a new class
class MotorBackwardsCommand(commands2.Command):
    
    # Inside the parameters of init im doing the same as the previous command
    def __init__(self, newSubsystem: NewSubsystemClass):
        super().__init__()
        self.newSub = newSubsystem
        self.addRequirements(newSubsystem)
        
    # Rest of the methods work the same as the ones for the previous command
    def initialize(self):
        logger.info("Motors Backwards")
        
    def execute(self):
        self.newSub.motorGroupBackward()
        
    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted: bool):
        self.newSub.stopMotors()
        
# This class is meant to be used in the false state of if the button is currently being pressed
class StopMotorsCommand(commands2.Command):
    def __init__(self, newSubsystem: NewSubsystemClass):
        super().__init__()
        self.newSub = newSubsystem
        self.addRequirements(newSubsystem)
        
    def initialize(self):
        logger.info("Motors Stop")
        
    def execute(self):
        self.newSub.stopMotors()
        
    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted: bool):
        self.newSub.stopMotors()