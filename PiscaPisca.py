import machine
import time

button1 = machine.Pin(26, machine.Pin.IN)
led1 = machine.Pin(14, macPiscahine.Pin.OUT)
button2 = machine.Pin(27, machine.Pin.IN)
led2 = machine.Pin(12, machine.Pin.OUT)

while True:
    
    button_state1 = button1.value()
    print(button_state1)
    button_state2 = button2.value()
    print(button_state2)
    
    if (button_state1):
        led1.on()
    else:
        led1.off()

    if(button_state2):
        led2.on()
    else:
        led2.off()

    if(button_state1 and button_state2):
        led2.on()
        time.sleep(0.1)
        led2.off()
        time.sleep(0.1)
        led1.on()
        time.sleep(0.1)
        led1.off()
        time.sleep(0.1)

3,
