class Battery:
    def __init__(self) -> None:
        self._energy = 10
    
    def get_energy(self) -> int:
        return self._energy
    
    def set_energy(self) -> None:
        self._energy += 2
    
    def decreaseEnergy(self) -> None:
        self._energy -= 1

class FlashLamp:
    def __init__(self) -> None:
        self._status = False
        self._battery = None

    def setBattery(self, Battery) -> None:
        self._battery = Battery

    def getBatteryInfor(self) -> int:
        return self._battery._energy
    
    def turnOn(self) -> None:
        if self.getBatteryInfor() > 0:
            print("Turn on the light!")
            self._status = True
            self._battery.decreaseEnergy()
        else:
            print("Cann't turn on the light because run out of the energy!")

    def turnOff(self) -> None:
        print("The light has been turned off!")
        self._status = False

class TestFlashLamp:
    def main():
        Banasonic = Battery()
        TheLight = FlashLamp()
        TheLight.setBattery(Banasonic)
        for i in range(5):
            TheLight.turnOn()
            TheLight.turnOff()

        TheLight._battery.set_energy()
        TheLight._battery.set_energy()

        print("Energy of FlashLamp :",TheLight.getBatteryInfor())

        for i in range(10):
            TheLight.turnOn()
            TheLight.turnOff()
        
        print("Energy of FlashLamp :",TheLight.getBatteryInfor())

if __name__ == "__main__":
    TestFlashLamp.main()
    


    