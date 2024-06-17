from machine import Pin, ADC
import time

pir_sensor = Pin(22, Pin.IN)
pir_buzzer = Pin(13, Pin.OUT)

def sensor():
    while True:
        if pir_sensor.value() == 1:
            print("Movimento detectado!")
            time.sleep(1)
            pir_buzzer.on()
            time.sleep(0.5)
            pir_buzzer.off()
        else:
            print("Nenhum movimento")
            time.sleep(1)

        
sensor()
