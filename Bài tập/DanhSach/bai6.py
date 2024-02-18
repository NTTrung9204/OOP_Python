class Battery:
    def __init__(self):
        self.energy = 10

    def set_energy(self, energy):
        self.energy = energy

    def get_energy(self):
        return self.energy

    def decrease_energy(self):
        self.energy -= 2


class FlashLamp:
    def __init__(self):
        self.status = False
        self.battery = None

    def set_battery(self, battery):
        self.battery = battery

    def get_battery_info(self):
        if self.battery:
            return self.battery.get_energy()
        else:
            return 0

    def turn_on(self):
        if self.battery and self.battery.get_energy() > 0:
            self.status = True
            print("FlashLamp is on. Light is on." if self.status else "FlashLamp is off.")

    def turn_off(self):
        self.status = False
        print("FlashLamp is off.")


class TestFlashLamp:
    def main(self):
        battery = Battery()
        flashlamp = FlashLamp()
        flashlamp.set_battery(battery)

        print("Initial battery energy:", battery.get_energy())

        for i in range(10):
            flashlamp.turn_on()
            flashlamp.turn_off()
            battery.decrease_energy()

        print("Remaining battery energy:", battery.get_energy())


if __name__ == "__main__":
    test = TestFlashLamp()
    test.main()
