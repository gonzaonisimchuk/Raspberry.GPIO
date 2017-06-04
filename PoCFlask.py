from flask import Flask, jsonify, make_response, request, abort
import RPi.GPIO as GPIO

app = Flask(__name__)
devices= {5: "Bano",
6: "P1",
13: "P2",
19: "P3",
21: "P4",
26: "Afuera",
27: "Test" }

def setupPines():
	GPIO.setup(27, GPIO.OUT)

def encender(pin):
	GPIO.output(pin, True)
	print ("encender pin:" + str(pin))
	
def apagar(pin):
	GPIO.output(pin, False)
	print ("apagar pin:" + str(pin))

@app.route('/',methods = ['GET'])
def index():
	if GPIO.input(27) == 0:
		encender(27)
	else:
		apagar(27)
	return "Hola"

@app.route('/<id>',methods = ['GET'])
def indexid(id):
	id = int(id)
	if devices.get(id) == None:
		return "Dispositivo no encontrado"
	if GPIO.input(id) == 0:
		encender(id)
		return str(id) + " encendido"
	else:
		apagar(id)
		return str(id) + " apagado"
#	return "Hola"

@app.route('/dispositivos',methods = ['GET'])
def dispositivos():
	return str(devices)
	
#capturadores de errores
#@app.errorhandler(404)
#def not_foud(error):
#	return "error 404"

	
#@app.errorhandler(405)
#def not_foud(error):
#	return "error 405"

if __name__ == '__main__':
	print ("inicio")
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	setupPines()
	app.run(debug = True, host='0.0.0.0', port=80)
