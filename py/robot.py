__author__ = "Sidd Karamcheti, Calvin Huang"

try:
    import wpilib
except ImportError:
    from pyfrc import wpilib
from config import sp, lstick, drive_macro, auto_sp
import sys


def CheckRestart():
    if lstick.button10:
        sys.exit()


class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        while self.IsDisabled():
            CheckRestart()
            wpilib.Wait(0.01)

    def Autonomous(self):
        self.GetWatchdog().SetEnabled(False)
        drive_macro.initialize()
        while self.IsAutonomous() and self.IsEnabled():
            CheckRestart()
            auto_sp.poll()
            drive_macro.perform()
            wpilib.Wait(0.01)
        drive_macro.disable()

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            CheckRestart()

            # Motor control

            sp.poll()

            wpilib.Wait(0.04)
            #Testing Github editor


def run():
    robot = MyRobot()
    robot.StartCompetition()
    return robot

if __name__ == '__main__':
    wpilib.run()
