from collections.abc import Callable
from pymodbus import FramerType
from pymodbus.client import ModbusSerialClient
import time

class ModbusSerialClientService(ModbusSerialClient):
    
    def __init__(self, port: str ='/dev/ttyUSB0', framer: FramerType = FramerType.RTU, 
                 baudrate: int = 9600, bytesize: int = 8, parity: str = "N",
                 stopbits: int = 1, handle_local_echo: bool = False, 
                 name: str = "comm", reconnect_delay: float = 0.1, 
                 reconnect_delay_max: float = 300, 
                 timeout: float = 3, retries: int = 3) -> None:
        super().__init__(port, framer, baudrate, 
                         bytesize, parity, stopbits, 
                         handle_local_echo, name, reconnect_delay, 
                         reconnect_delay_max, timeout, retries)