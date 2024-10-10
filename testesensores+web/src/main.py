import serial
import time
import mysql.connector

ser = serial.Serial('COM3', 9600, timeout=1) # Iniciando a conexão serial
con = mysql.connector.connect(host='paparella.com.br', database='paparell_iot', user='paparell_iot', password='senai2024') # Conectando no banco

# Conferindo se a conexão com o banco foi bem sucedida
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado, versão: ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)


time.sleep(2) # Tempinho pq ninguém é de ferro

cont = 10 #ler o serial
for i in range(cont):
    line = ser.readline()
    string_data = line
    print(string_data)
    
    # Inserir no banco
    sql = "INSERT INTO bosch (nome_aluno, nome_sensor, valor_sensor) VALUES (%s, %s, %s)"
    val = ("Juliana", "Sensor de touch", string_data)
    cursor.execute(sql, val)


    
# Mostrar as tabelas
cursor.execute("SHOW TABLES")
for i in cursor:
    print("Minhas tabelas: ", i)

con.commit()

print(cursor.rowcount, "Dados gravados")
    

cursor.execute("SELECT * FROM bosch")

myresult = cursor.fetchall()

for i in myresult:
    print(i)

ser.close()