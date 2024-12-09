import wpilib
import wpimath.controller

import commands2
import commands2.cmd
import commands2.button

# Import Constants
import constants
from constants import OP

# Import Subsystem
import subsystems.newSubsystem
import subsystems.photonVisionSubsystem

# Import Commands
from commands.newCommands import MotorBackwardsCommand, MotorForwardCommand, StopMotorsCommand
from commands.visionCommand import displayingData, displaySeenAprilTags


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.  Since
    Command-based is a "declarative" paradigm, very little robot logic should
    actually be handled in the :class:`.Robot` periodic methods (other than
    the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # Define the robot's subsystems
        self.newSubsystem = subsystems.newSubsystem.NewSubsystemClass()
        self.visionSunsystem = subsystems.photonVisionSubsystem.visionSubsystem()

        # Assign the driver's controller
        self.DriverController = commands2.button.CommandXboxController(OP.driver_joystick_port)
        self.OperatorController = commands2.button.CommandXboxController(OP.operator_joystick_port)


        # Configure the button bindings
        self.configureButtonBindings()


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        
        # In the true state of this button it will run the MotorBackwardsCommand & in the false state it will run StopMotorsCommand
        # To assign a command to button we first need to start off with the controller we want to assign the button from wether it's from the operator or the driver port
        # afterwards we use the method that corresponds to the button we will be using (In this example it is the left bumper button)
        # after we tell it under which state do we want the following command to run (we normally use whileFalse/whileTrue)
        # Lastly inside of the parameters of whileTrue/whileFalse we put the command we want to run & we create another set of parameters and inside there we put the subsystem the command requires to be able to run
        
        self.OperatorController.leftBumper().whileTrue(MotorBackwardsCommand(self.newSubsystem))
        self.OperatorController.leftBumper().whileFalse(StopMotorsCommand(self.newSubsystem))
        
        # Same thing as before but now were using the right bumper and the MotorForwardCommand
        # self.OperatorController.rightBumper().whileTrue(MotorForwardCommand(self.newSubsystem))
        # self.OperatorController.rightBumper().whileFalse(StopMotorsCommand(self.newSubsystem))
        
        self.OperatorController.a().whileTrue(displayingData(self.visionSunsystem))
        
        self.OperatorController.b().whileTrue(displaySeenAprilTags(self.visionSunsystem))

    def getAutonomousCommand(self):
        return None