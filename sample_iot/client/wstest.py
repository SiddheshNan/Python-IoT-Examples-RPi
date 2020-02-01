from websocket import create_connection
import websocket
import threading
import time
import json
import Adafruit_DHT

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
p1=19
p2=26
GPIO.setup(p1,GPIO.OUT)
GPIO.setup(p2,GPIO.OUT)

GPIO.output(p1, 1)
GPIO.output(p2, 1)

def on_message(ws, message):
    # print '\nRecieved: ' + message
    var = json.loads(message)
    # print(var)

    if 'switch' in var:
        print(var)
        if var['switch'] == 1:
            if var['value']:
                GPIO.output(p1, 1)
            else:
                GPIO.output(p1, 0)
        # else:
        #     GPIO.output(dev1, var['value'])
        if var['switch'] == 2:
            if var['value']:
                GPIO.output(p2, 1)
            else:
                GPIO.output(p2, 0)
        # else:
        #     GPIO.output(dev2, var['value'])


def on_error(ws, error):
    print (error)


def on_close(ws):
    print ("### closed ###")


def on_open(ws):
    def run(*args):
        while -1:
            hum,temp=Adafruit_DHT.read_retry(11,2)
            data = {"hum": str(hum),"temp":str(temp)}
            data = json.dumps(data)
            #var = raw_input("Enter data to send: ")
            ws.send(data)

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(False)
    # global uid
    # uid = raw_input("Please enter UID: ")
    ws = websocket.WebSocketApp("ws://127.0.0.1:8888/ws",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()
