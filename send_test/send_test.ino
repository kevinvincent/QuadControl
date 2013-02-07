/*
  Software serial multple serial test
 
 Receives from the hardware serial, sends to software serial.
 Receives from software serial, sends to hardware serial.
 
 The circuit: 
 * RX is digital pin 10 (connect to TX of other device)
 * TX is digital pin 11 (connect to RX of other device)
 
 Note:
 Not all pins on the Mega and Mega 2560 support change interrupts, 
 so only the following can be used for RX: 
 10, 11, 12, 13, 50, 51, 52, 53, 62, 63, 64, 65, 66, 67, 68, 69
 
 Not all pins on the Leonardo support change interrupts, 
 so only the following can be used for RX: 
 8, 9, 10, 11, 14 (MISO), 15 (SCK), 16 (MOSI).
 
 created back in the mists of time
 modified 25 May 2012
 by Tom Igoe
 based on Mikal Hart's example
 
 This example code is in the public domain.
 
 */
#include <SoftwareSerial.h>
#include <Servo.h> 

const char startOfNumberDelimiter = '<';
const char endOfNumberDelimiter   = '>';

SoftwareSerial mySerial(10, 11); // RX, TX
Servo myservo;  // create servo object to control a servo 


void setup()  
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
  
  Serial.println("Started Software Serial...");
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
}
  
void processNumber (const long n) {
  myservo.write(n);
  Serial.print(n);
  Serial.print("\n");
}  // end of processNumber
  
void processInput ()
  {
  static long receivedNumber = 0;
  static boolean negative = false;
  
  byte c = mySerial.read();
  
  switch (c)
    {
      
    case endOfNumberDelimiter:  
      if (negative) 
        processNumber (- receivedNumber); 
      else
        processNumber (receivedNumber); 

    // fall through to start a new number
    case startOfNumberDelimiter: 
      receivedNumber = 0; 
      negative = false;
      break;
      
    case '0' ... '9': 
      receivedNumber *= 10;
      receivedNumber += c - '0';
      break;
      
    case '-':
      negative = true;
      break;
      
    } // end of switch  
  }  // end of processInput
  
void loop () {
  if (mySerial.available())
    processInput();
}

void terminal()
{
  while(true) {
  if (mySerial.available())
    Serial.write(mySerial.read());
  if (Serial.available())
    mySerial.write(Serial.read());
  }
}
