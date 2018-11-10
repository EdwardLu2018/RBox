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

  Serial.println("Starting...");
}

void loop() {
  while (Serial.available()) {
    data = Serial.read();
    Serial.println(data);
    Serial.println(data - 48, DEC);
  }

  if (data == '2') {
    digitalWrite (motorTwo, HIGH);
    delay(500);
    digitalWrite (motorTwo, LOW);
    delay(500);
  }

  else if (data == '1') {
    digitalWrite (motorOne, HIGH);
    delay(500);
    digitalWrite (motorOne, LOW);
    delay(500);
  }

  else if (data == '0') {
    digitalWrite (motorZero, HIGH);
    delay(500);
    digitalWrite (motorZero, LOW);
    delay(500);
  }

}
