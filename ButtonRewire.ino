/*
  Button

  Turns on and off a light emitting diode(LED) connected to digital pin 13,
  when pressing a pushbutton attached to pin 2.

  The circuit:
  - LED attached from pin 13 to ground
  - pushbutton attached to pin 2 from +5V
  - 10K resistor attached to pin 2 from ground

  - Note: on most Arduinos there is already an LED on the board
    attached to pin 13.

  created 2005
  by DojoDave <http://www.0j0.org>
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Button
*/

// constants won't change. They're used here to set pin numbers:
const int buttonInPin = 2;     // the number of the pushbutton pin
const int keyInPin = 8;
const int ledOutPin = 5;
const int buttonOutPin = 4;

// variables will change:
int buttonState = 0;  // variable for reading the pushbutton status
int keyState = 0;
int justTurned = 0;
int pressedYet = 0;

void setup() {
  // initialize the pushbutton pin as an input:
  pinMode(buttonInPin, INPUT_PULLUP);
  pinMode(keyInPin, INPUT);
  pinMode(buttonOutPin, OUTPUT);
  pinMode(ledOutPin, OUTPUT);
  digitalWrite(buttonOutPin, HIGH);
  Serial.begin(9600);
  Serial.print("hello there\n version 0.0.6\n");
}

void loop() {
  // read the state of the pushbutton value:
  keyState = digitalRead(keyInPin);
  Serial.print (keyState + "\n");
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (keyState == HIGH) {
    if (justTurned == 0) {
      Serial.print ("Key Just Turned\n");
      justTurned = 1;
      digitalWrite(ledOutPin, HIGH);
  //    delay(5000);
    }
    if (justTurned == 1) {
      digitalWrite(buttonInPin, LOW);
      buttonState = digitalRead(buttonInPin);
        if (pressedYet == 0) {
          if (buttonState == HIGH) {
            digitalWrite(ledOutPin, LOW);
            Serial.print("button\n");
            pressedYet = 1;
            }
        }
    }
  }
  else {
    justTurned = 0;
    pressedYet = 0;
    digitalWrite(ledOutPin, LOW);
  }
}
