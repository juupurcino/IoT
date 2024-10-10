#include <Arduino.h>
#include <Adafruit_Sensor.h>

const int pinoSensor = 2; 
const int pinoLed = 3; 
 
void setup() {

  Serial.begin(9600);
  pinMode(pinoSensor, INPUT); 
  pinMode(pinoLed, OUTPUT); 
}
 
void loop() {
  if (digitalRead(pinoSensor) == HIGH){ 
    digitalWrite(pinoLed, HIGH); 
    Serial.println("Tocando");
  }
  else{ 
    digitalWrite(pinoLed,LOW); 
    Serial.println("nao tocando");
  } 
  delay(200); 
}