from video.board.board_controller import Board

class BoardRestController:
    def __init__(self) -> None:
        self.board : Board = Board()

    def  setPin(self,pin,state):
        match state:
            case 0:
                self.board.pinOff(pin)
            case 1:
                self.board.pinOn(pin)

