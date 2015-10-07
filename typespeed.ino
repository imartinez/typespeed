#include <Servo.h>

// Simple sketch that receives a value via Serial
// and set a servo angle to that value.
// Used by typespeed.py to measure typing speed.

Servo servo1;

void setup() {

  pinMode(1,OUTPUT);
  servo1.attach(9); //PWM PIN 9
  Serial.begin(9600);
  Serial.println("Ready!");

}

void loop() {

  static int v = 0;

  if ( Serial.available()) {
    int value = Serial.parseInt();
    Serial.println(value);
    servo1.write(value);
    Serial.flush();
  }

} 
