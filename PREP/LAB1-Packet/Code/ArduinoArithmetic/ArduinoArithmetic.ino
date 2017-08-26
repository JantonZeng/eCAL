
char demo;

void setup(){
   Serial.begin(9600); 
}

void loop(){
  if( Serial.available() ){
    demo = Serial.read();
    
    if( '0' == demo ){
        Serial.println("Demo 0: Numbers");
        int r;
        r = 9/10*100; // r is 0
        Serial.println(">> int r = 9/10*100;");
        Serial.print("r is ");
        Serial.println(r);
        
        r = 9*100/10; // r is 90
        Serial.println(">> r = 9*100/10;");
        Serial.print("r is ");
        Serial.println(r);
        
        r = (9*100)*(1/10); // r is 0
        Serial.println(">> r = (9*100)*(1/10);");
        Serial.print("r is ");
        Serial.println(r);
        
        r = 32767 + 1; // r is -32768
        Serial.println(">> r = 32767 + 1;");
        Serial.print("r is ");
        Serial.println(r);
        
        Serial.println();
        Serial.println();
        Serial.println();
        Serial.println();
    }else if( '1' == demo ){
        Serial.println("Demo 1: ");
        Serial.println("Type Casting:");
        int r;
        // Type Casting
        r = (float) 9/10*100; // r is 90
        Serial.println(">> int r = (float) 9/10*100;");
        Serial.print("r is ");
        Serial.println(r,DEC);
        Serial.println();
        
        // Type Conversion
        Serial.println("Type Conversion:");
        r = float(9)/10*100;  // r is 90
        Serial.println(">> r = float(9)/10*100; ");
        Serial.print("r is ");
        Serial.println(r,DEC);
        
        float f = float(r);
        Serial.println(">> float f = float(r);");
        Serial.print("f is ");
        Serial.println(f,6);
        
        Serial.println();
        Serial.println();
        Serial.println();
        Serial.println();
        
     }else if( '2' == demo ){ 
        
        Serial.println("Demo 2: Float Precision");
        float f = 49 + 1.01;
        Serial.println(">> float f = 49 + 1.01;");
        Serial.print("f is ");
        Serial.println(f,6);
  
        f = f + 0.001;
        Serial.println(">> f = f + 0.001;");
        Serial.print("f is ");
        Serial.println(f,6);
        
        f = f*2;
        Serial.println(">> f = f*2;");
        Serial.print("f is ");
        Serial.println(f,6);
        
        Serial.println();
        Serial.println();
        Serial.println();
        Serial.println();
    }else if( '3' == demo ){
      
        Serial.println("Demo 3: Characters");
        int r;
        r = int('a'); // r is 97
        Serial.println(">> int r = int('a');");
        Serial.print("r is ");
        Serial.println(r);
        
        r = int('2'); // r is 50
        Serial.println(">> int r = int('2');");
        Serial.print("r is ");
        Serial.println(r);
        
        char c = 'a' + 1;
        Serial.println(">> char c = 'a' + 1;");
        Serial.print("c is ");
        Serial.println(c);
        
        c = 99; // c is 'c' 
        Serial.println(">> char c = 99;");
        Serial.print("c is ");
        Serial.println(c);
        
        Serial.println();
        Serial.println();
        Serial.println();
        Serial.println();
    }
    
    delay(500); 
  }
  
}
/*
    int r;
    r = 9/10*100; // r is 0
    r = 9*100/10; // r is 90
    r = (9*100)*(1/10); // r is 0
    
    r = 32767 + 1; // r is -32768
    
    int r;
    // Type Casting
    r = (float) 9/10*100; // r is 90
    // Type Conversion
    r = float(9)/10*100;  // r is 90
    
    int r;
    r = int('a'); // r is 97
    r = int('2'); // r is 50
    
    char c = 'a';
    c++;    // c is 'b'
    c = 99; // c is 'c'
    
    
    char Str1[15];
    char Str2[8] = {'a', 'r', 'd', 'u', 'i', 'n', 'o'};
    char Str3[8] = {'a', 'r', 'd', 'u', 'i', 'n', 'o', '\0'};
    char Str4[ ] = "arduino";
    char Str5[8] = "arduino";
    char Str6[15] = "arduino";
    
    */
