from video.modbus.model.serial_model import ModbusPayload
from video.modbus.serial.serial_controller import ModbusSerialClientService



class ModbusSerialRestController:
    def __init__(self) -> None:
        self.service = ModbusSerialClientService(port='/dev/ttyUSB0',baudrate=9600)

    def execute(self,command:ModbusPayload):
        self.service.connect()
        self.service.write_coil(command.output, command.outputValue, slave=command.slaveId)
        self.service.close()
