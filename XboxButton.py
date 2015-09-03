# import the buttons package from wpilib
from wpilib import buttons


class XboxButton(buttons.JoystickButton):
    '''
    A subclass of JoystickButton that offers a poll function
    which should clear up issues
    '''
    def __init__(self, controller, button_num):
        super().__init__(controller, button_num)

    def poll(self):
        rtn_val = self.get()
        for i in range(0, 10):
            pass
        return rtn_val
