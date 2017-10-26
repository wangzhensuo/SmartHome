import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(38, GPIO.OUT)
    GPIO.output(38, GPIO.LOW)

def destroy():
    GPIO.output(38, GPIO.LOW)
    GPIO.setup(38, GPIO.IN)

def turnOffLed():
    setup()
    GPIO.output(38, GPIO.LOW)

def turnOnLed():
    GPIO.output(38, GPIO.HIGH)
    GPIO.cleanup()
#    destroy()
    

if __name__=="__main__":
    turnOnLed()#此处作为测试代码设置的，import的时候并不运行，在单独跑led.py时候运行
    time.sleep(2)
    turnOffLed()
