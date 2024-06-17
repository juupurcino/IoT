from machine import Pin
import time

# Configuração dos pinos do LCD
rs = Pin(2, Pin.OUT)
e = Pin(4, Pin.OUT)
d4 = Pin(5, Pin.OUT)
d5 = Pin(18, Pin.OUT)
d6 = Pin(19, Pin.OUT)
d7 = Pin(21, Pin.OUT)
button1 = Pin(13, Pin.IN)
espaco = 15
pontos = 0

def pulse_enable():
    e.on()
    time.sleep_us(1)
    e.off()
    time.sleep_us(50)

def send_nibble(data):
    d4.value((data >> 0) & 1)
    d5.value((data >> 1) & 1)
    d6.value((data >> 2) & 1)
    d7.value((data >> 3) & 1)
    pulse_enable()

def send_byte(data, rs_value):
    rs.value(rs_value)
    send_nibble(data >> 4)  # Envia o nibble superior
    send_nibble(data & 0x0F)  # Envia o nibble inferior

def lcd_command(cmd):
    send_byte(cmd, 0)

def lcd_data(data):
    send_byte(data, 1)

def lcd_init():
    time.sleep(0.05)
    rs.off()
    e.off()
    send_nibble(0x03)
    time.sleep_ms(5)
    send_nibble(0x03)
    time.sleep_us(150)
    send_nibble(0x03)
    send_nibble(0x02)
    lcd_command(0x28)  # Função set: 4 bits, 2 linhas, 5x8 pontos
    lcd_command(0x0C)  # Display on, cursor off, blink off
    lcd_command(0x06)  # Entry mode set: incrementa e sem shift
    lcd_command(0x01)  # Limpa o display
    time.sleep_ms(2)

def limpa():
    lcd_command(0x01)

def lcd_puts(text):
    for char in text:
        lcd_data(ord(char))

def primeira_linha():
    lcd_command(0x80)
    
def segunda_linha():
    lcd_command(0xc0)
    
def pulo():
    primeira_linha()
    lcd_puts(' 웃')

lcd_init()

flag = 0
while True:
    
    if(espaco < 0):
        espaco = 15
    
    #flexa ficar andando
    button_state = button1.value()
    obstaculo = espaco * ' ' +'<='
    segunda_linha()
    lcd_puts(obstaculo)
    primeira_linha()
    lcd_puts("               " + str(pontos))
    
    if(button_state == 1 and flag == 0):
        pulo()
        jump = 1
        pontos += 1
        flag = 1
             
    else:
        segunda_linha()
        lcd_puts(' 웃')
        jump = 0
        flag = 0
    
    time.sleep(0.2)
    espaco -= 1
    limpa()
    time.sleep(0.2)
    
    if(espaco == 1 and jump !=1):
        limpa()
        primeira_linha()
        lcd_puts("        GAME")
        segunda_linha()
        lcd_puts("      OVER")
        break

    
    
    
    
    
    
    


