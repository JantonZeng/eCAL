   /*
    SerialEcho
    This example code is in the public domain.
   */

  int incomingByte = 0;   // for incoming serial data
     
    void setup(){
      // Initialize at 9600 bps
      Serial.begin(9600);
    }
    
    void loop(){
      // Check if incoming content has been received
      // by Serial port
      if(Serial.available() > 0) {
        // Read the next incoming byte
        incomingByte = Serial.parseInt();
        // variable incomingByte is a byte in Hexidecimal representing char we sent

        // say what you got:
        Serial.print(incomingByte);
        // .write knows incomingByte is a byte, and sends a byte
        // then your laptop interprets this byte as a char using ASCII table
        Serial.print(';'); 
        // .print treats incomingByte like a number, and sends the number
        // then your laptop prints the literal number in incomingByte
      }

      // Add delay for stability
      delay(10);
    }
