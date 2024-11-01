from dataclasses import dataclass


@dataclass
class ModbusPayload:
    driverType: str
    modbusIp: str
    modbusPort: int
    output: int
    outputValue: bool
    portName: str
    slaveId: int

@dataclass
class ModbusResponse():
    outcome: int
    status: bool
