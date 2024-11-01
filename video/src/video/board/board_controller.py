from  gpiozero import LED

class Board:
    def __init__(self) -> None:
        self.pins_used ={}

    def _testAndSet(self,pin):
        ledPin: LED = self.pins_used.get(pin)
        if ledPin is None:
            ledPin = LED(pin)
            self.addOutputPin(pin,ledPin)
        return ledPin
    
    def pinOn(self,pin):
        ledPin: LED = self._testAndSet(pin)
        ledPin.on()

    def pinOff(self,pin):
        ledPin: LED = self._testAndSet(pin)
        ledPin.off()

    def addOutputPin(self,pin,ledPin):
        self.pins_used[pin]=ledPin