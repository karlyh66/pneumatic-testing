class MechController:

    def __init__(self, driver_joystick, xbox_controller): # mechanisms belong in arguments
        # define mechanisms here
        self.driver_joystick = driver_joystick
        self.xbox_controller = xbox_controller
        driver_joystick.add_listener(self._driver_joystick_listener)
        xbox_controller.add_listener(self._xbox_controller_listener)

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == 'a_button': #1/4 extension, 1001
            s_a.set(True);
            s_b.set(False);
            s_c.set(False);
            s_d.set(True);
        elif state_id == 'b_button': #1/2 extension, 1101
            s_a.set(True);
            s_b.set(True);
            s_c.set(False);
            s_d.set(True);
        elif state_id == 'x_button': #full extension, 1111
            s_a.set(True);
            s_b.set(True);
            s_c.set(True);
            s_d.set(True);
        elif state_id == 'back_button': #back, 0000
            s_a.set(False);
            s_b.set(False);
            s_c.set(False);
            s_d.set(False);

    def _driver_joystick_listener(self, sensor, state_id, datum):
        pass