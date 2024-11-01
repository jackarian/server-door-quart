from quart import Quart
from quart_schema import QuartSchema, validate_request, validate_response
from quart import jsonify
import time
import datetime
from quart_babel import Babel
from quart_babel import format_datetime
from babel.dates import get_timezone, UTC
from video.board.board_rest import BoardRestController
from video.i2c.smbus_controller import SmbusController
from video.modbus.model.serial_model import ModbusPayload, ModbusResponse
from video.modbus.serial.serial_rest import ModbusSerialRestController

app = Quart(__name__)
schema = QuartSchema(app)
babel  = Babel(app)
rbc = BoardRestController()
i2cc = SmbusController()
modbus = ModbusSerialRestController()



    
@app.get("/")
async def index():
    return   jsonify({
            "live": "OK",
            "timestamp": format_datetime(dt=datetime.datetime.now(get_timezone('Europe/Rome')),format='full',rebase=True)
            })

@app.get("/monitoraggio/gpio/pin/<int:pin>/<int:state>")
async def monitoraggio_gpio(pin,state):
       rbc.setPin(pin,state)
       return jsonify({
            "command": "OK",
            "timestamp": format_datetime(dt=datetime.datetime.now(get_timezone('Europe/Rome')),format='full',rebase=True)
            })

@app.get("/monitoraggio/gpio/register/<int:reg>/<int:pin>/<int:state>")
async def monitoraggio_i2c(reg,pin,state):
     i2cc.write(reg,pin,state)
     return jsonify({
            "command": "OK",
            "timestamp": format_datetime(dt=datetime.datetime.now(get_timezone('Europe/Rome')),format='full',rebase=True)
            })


@app.post("/monitoraggio/remoteio")
@validate_request(ModbusPayload)
@validate_response(ModbusResponse)
async def monitoraggio_remoto(data : ModbusPayload) -> ModbusResponse:
     modbus.execute(data)     
     return {"outcome": 0, "status": True}
     


def run() -> None:
    app.run()