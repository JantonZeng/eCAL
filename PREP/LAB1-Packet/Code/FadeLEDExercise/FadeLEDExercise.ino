    /*
      Fade LEDs
     
      This example code is in the public domain.
     */
     
    // Attached a LED with a 1k resistor to Pin 6
    int led = 7;
    
    void setup() {  // Setup routine runs once when you press reset:  
      // Initialize serial communication
      // at 9600 bits per second
      Serial.begin(9600);
      pinMode(led, OUTPUT);  // Initialize the digital pins as an output.
    }
    
    void loop() { // Loop routine runs over and over again forever:
      fadeLED(2);
    }
        
    // Fade LED function takes a time in 
    // seconds and fades the LED
    void fadeLED(int seconds){
      int timesteps = 100;
      for(int i=0;i<timesteps;i++){
        // Calculate the LED brightness
        // as a percentage (0 to 100)
        // Note: int cannot have decimals
        int percent = i*100/timesteps;
        // Calculate the LED brightness
        // as PWM output (0 to 255)
        // Note: percent*255/100 does not = percent/100*255
        int brightness = percent*255/100; 
        // Use analogWrite for PWM of a pin
        analogWrite(led, brightness);
        Serial.println(brightness);
        delay(seconds*1000/timesteps);
      }
      // Repeat in reverse
      for(int i=0;i<timesteps;i++){
        int percent = i*100/timesteps;
        int brightness = percent*255/100;
        analogWrite(led, 255-brightness);
        Serial.println(brightness);
        delay(seconds*1000/timesteps);
      }
    }
