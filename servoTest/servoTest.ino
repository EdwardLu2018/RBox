#include <Servo.h>
Servo servoA;
Servo servoB;
Servo servoC;

int data;
int motorZero = 2;
int motorOne = 4;
int motorTwo = 7;

void setup() {
  Serial.begin(9600); // initialize serial COM at 9600 baudrate
  pinMode(motorZero, OUTPUT);
  pinMode(motorOne, OUTPUT);
  pinMode(motorTwo, OUTPUT);// make the LED pin (13) as output
  digitalWrite (LED_BUILTIN, LOW);
 

  servoA.attach(9); // attaches the servo on pin 9  to the servo object
  servoB.attach(10); // attaches the servo on pin 10 to the servo object
  servoC.attach(11);

  Serial.println("Starting...");
}

void loop() {
  while (Serial.available()) {
    data = Serial.read();
    Serial.println(data);
    Serial.println(data - 48, DEC);
  }

  if (data == '2') {
    Serial.print("hi");
    digitalWrite(motorTwo, HIGH);
    digitalWrite(motorOne, LOW);
    digitalWrite(motorZero, LOW);
    servoC.write(10);
    delay(500);
    servoC.write(170);
    delay(500);
    servoC.write(10);
  }

  else if (data == '1') {
    digitalWrite(motorTwo, LOW);
    digitalWrite(motorOne, HIGH);
    digitalWrite(motorZero, LOW);
    servoB.write(10);
    delay(500);
    servoB.write(170);
    delay(500);
    servoC.write(10);
    
  }

  else if (data == '0') {
    digitalWrite(motorTwo, LOW);
    digitalWrite(motorOne, LOW);
    digitalWrite(motorZero, HIGH);
    servoA.write(10);
    delay(500);
    servoA.write(170);
    delay(500);
    servoC.write(10);
  }

}
