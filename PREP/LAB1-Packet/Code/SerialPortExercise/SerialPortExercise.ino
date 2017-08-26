    
    /*
     SerialPort
     This example code is in the public domain.
    */
    
    // Declare integer for counting the loops
    int count = 0; 
    
    void setup() {
      // Initialize serial communication
      // at 9600 bits per second
      Serial.begin(9600);
    }
    
    void loop() {
      // Print the count to the serial port
      Serial.println(count); 
      // Iterate the count
      count = count + 1; 
      // Same as:
      // count++;
      // count+=1
      delay(1000);
    }



