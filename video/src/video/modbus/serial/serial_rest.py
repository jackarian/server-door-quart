from video.modbus.model.serial_model import ModbusPayload
from video.modbus.serial.serial_controller import ModbusSerialClientService
from pymodbus import FramerType
from pymodbus.client import ModbusSerialClient


class ModbusSerialRestController:
    def __init__(self) -> None:
        self.service = ModbusSerialClient(port='/dev/ttyUSB1', framer = FramerType.RTU,
                 baudrate= 9600, bytesize= 8, parity= "N",
                 stopbits = 1, handle_local_echo = False,
                 name= "comm", reconnect_delay = 0.1,
                 reconnect_delay_max= 300,
                 timeout= 3, retries = 3)

    def execute(self,command:ModbusPayload):
        self.service.connect()
        self.service.write_coil(command.output, command.outputValue, device_id=command.slaveId)
        self.service.close()
