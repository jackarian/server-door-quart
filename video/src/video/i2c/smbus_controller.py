from smbus2 import SMBus


class SmbusController:
    def __init__(self) -> None:
        self.smb = SMBus(1)
        self.stackMap = { 1 :0x10, 2 :0x20, 3: 0x30, 4 : 0x40 }
        self.pinMap = {1 :0x01, 2 :0x02, 3: 0x03, 4 : 0x04 }
        self.stateMap = {0 : 0x00,1 :0xFF}

    def write(self,stack,pin,state):
        self.smb.write_i2c_block_data(self.stackMap[stack],self.pinMap[pin],[self.stateMap[state]])

if __name__ == '__main__':
    smb =SmbusController()
    smb.write(1,4,1)
    
    


