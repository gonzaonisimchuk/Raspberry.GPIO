from flask import Flask, jsonify, make_response, request, abort
import sys
import logging as log
import datetime as dt
import RPi.GPIO as GPIO

_host = '0.0.0.0'
_port = 4010

log.basicConfig(filename='{:%Y-%m-%d}.log'.format(dt.datetime.now()),
				level=log.DEBUG, 
				format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
devices = {
	"PBa": 5,
	"P1": 13,
	"P2": 26,
	"P3": 19,
	"P4": 6,
	"PAf": 21
	}

def setupPines():
	try:
		log.info("setupPines")
		for device in devices.values():
			log.info("GPIO.OUT: " + str(device))
    			GPIO.setup(device, GPIO.OUT)
	except:
		log.exception(sys.exc_info()[0])

def encender(pin):	
	GPIO.output(pin, True)
	log.debug("encender pin:" + str(pin))
	
def apagar(pin):
	GPIO.output(pin, False)
	log.debug("apagar pin:" + str(pin))

@app.route('/',methods = ['GET'])
def index():
	return "Sitema funcionando"

@app.route('/<id>',methods = ['GET'])
def indexid(id):
	pin = devices.get(id.upper())
	if pin == None:
		log.debug("Dispositivo no encontrado: " + id)
		return "Dispositivo no encontrado"
	if GPIO.input(pin) == 0:
		encender(pin)
		message = "{ dispositivo: " + id + ", pin: " + str(pin) + ", estado: encendido }"
		log.info(message)
		return message
	else:
		apagar(pin)
		message = "{ dispositivo: " + id + ", pin: " + str(pin) + ", estado: apagado }"
		log.info(message)
		return message

@app.route('/dispositivos',methods = ['GET'])
def dispositivos():
	log.debug("consulta dispositivos: " + str(devices))
	return str(devices)
	
# capturadores de errores
@app.errorhandler(404)
def not_foud(error):
	return "error 404"

	
@app.errorhandler(405)
def not_foud(error):
	return "error 405"

if __name__ == '__main__':
	log.info("Inicio")
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	setupPines()
	app.run(debug = False, host=_host, port=_port)
