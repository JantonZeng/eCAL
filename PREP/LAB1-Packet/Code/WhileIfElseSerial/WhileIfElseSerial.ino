  /*
    While, If, Else if, and Else
   
    This example code is in the public domain.
  */
   
  int count = 0;
  int maxCount = 20;
  
  // Setup routine runs once when you press reset
  void setup() {  
      // Initialize serial communication at 9600 bits per second
      Serial.begin(9600);
  }
  
  // Loop routine runs over and over again forever
  void loop() { 
      while( count <= maxCount ){
          Serial.print("count is ");
          Serial.println(count);
          if( count <= 5 ){
            // Do something is count is
            // less than or equal to 5
            Serial.println("count is <= 5");
          }else if( count <= 10 ){
            // Do something if count  
            // is > 5 and <= 10
            Serial.println("count is <= 10");
          }else if( count <= 15 ){
            // Do something if count  
            // is > 10 and <= 15
            Serial.println("count is <= 15");
          }else{
            // For all other cases,
            // (i.e. count is > 15) 
            // do something else
            Serial.println("count is > 15");
          }
          
          if( count < 5 || count > 10 ){
            Serial.println("Or");
          }else if( count > 5 && count < 10 ){
            Serial.println("And");
          }
          delay(500);
          count++;
      }
      
      Serial.println("While Loop Completed");
      delay(10000);
  }


  

