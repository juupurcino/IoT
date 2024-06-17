from machine import ADC, Pin
import time

# Configura o pino ADC onde o potenciômetro está conectado
potenciometro = ADC(Pin(14))
potenciometro.width(ADC.WIDTH_12BIT)  # Configura a resolução do ADC para 12 bits (0-4095)
potenciometro.atten(ADC.ATTN_11DB)    # Configura a atenuação para o range de 0-3.6V

# Configuração dos pinos do LCD
rs = Pin(2, Pin.OUT)
e = Pin(4, Pin.OUT)
d4 = Pin(5, Pin.OUT)
d5 = Pin(18, Pin.OUT)
d6 = Pin(19, Pin.OUT)
d7 = Pin(23, Pin.OUT)
sensor_luz = Pin(22, Pin.IN)

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

# Limpar tudo
def limpa():
    lcd_command(0x01)

#Printa no lcd
def print_lcd(text):
    for char in text:
        lcd_data(ord(char))

def primeira_linha():
    lcd_command(0x80)
    
def segunda_linha():
    lcd_command(0xc0)

# Função para ir até uma determinada casa   
def go_to(value):
    lcd_command(128 + value)

# Função principal para ler o potenciômetro
# def read_potentiometer():
#     
#     lcd_init()  # Inicializa o LCD uma vez antes de usar
#     while True:
#         pot_value = round((potenciometro.read() * 16) / 4095)
#         print("Valor do potenciômetro:", pot_value)
#         go_to(pot_value)                                 
#         print_lcd("J")  # Envia o texto para o LCD
#         time.sleep(2)
#         limpa()
#         time.sleep(1)
# 
# Chama a função principal
# read_potentiometer()

while True:
    print(sensor_luz.value())
    time.sleep(1)
