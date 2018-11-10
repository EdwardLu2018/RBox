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

  servoA.attach(motorZero); // attaches the servo on pin 9  to the servo object
  servoB.attach(motorOne); // attaches the servo on pin 10 to the servo object
  servoC.attach(motorTwo);

  Serial.println("Starting...");
}

void loop() {
  while (Serial.available()) {
    data = Serial.read();
    Serial.println(data);
    Serial.println(data - 48, DEC);
  }

  if (data == '2') {
    servoC.write(10);
    delay(500);
    servoC.write(170);
    delay(500);
  }

  else if (data == '1') {
    servoB.write(10);
    delay(500);
    servoB.write(170);
    delay(500);
  }

  else if (data == '0') {
    servoA.write(10);
    delay(500);
    servoA.write(170);
    delay(500);
  }

}
