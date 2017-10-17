import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT,initial=GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)

def destroy():
    GPIO.output(20, GPIO.HIGH)
    GPIO.setup(20, GPIO.IN)
    GPIO.output(21, GPIO.HIGH)
    GPIO.setup(21, GPIO.IN)

def turnOnLed():
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

def turnOffLed():
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
#    GPIO.cleanup()
    destroy()
    

if __name__=="__main__":
    time.sleep(2)
    turnOnLed()#此处作为测试代码设置的，import的时候并不运行，在单独跑led.py时候运行
    time.sleep(2)
    turnOffLed()
