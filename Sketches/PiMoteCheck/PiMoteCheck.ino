#include <PSTRStrings.h>
//#define DEBUGIT
unsigned long timeout = 0;
int state = 1;
#define NUMBER_OF_COMMANDS 15
PSTRStrings commands = PSTRStrings (NUMBER_OF_COMMANDS);

void setup ()
{
  Serial.begin (115200);
  for (int i=0; i<4; i++)
  {
    pinMode (i+8,OUTPUT);
    digitalWrite (i+8,1);
  }  
  commands.addString ( PSTR ( "login: " ) );             //  0
  commands.addString ( PSTR ( "Press 1 + 2" ) );         //  1
  commands.addString ( PSTR ( "Press some buttons!" ) ); //  2
  commands.addString ( PSTR ( "Plus Button pressed" ) ); //  3 
  commands.addString ( PSTR ( "Minus Button pressed") ); //  4 
  commands.addString ( PSTR ( "Button A pressed" ) );    //  5 
  commands.addString ( PSTR ( "Button B pressed" ) );    //  6 
  commands.addString ( PSTR ( "Button 1 pressed" ) );    //  7 
  commands.addString ( PSTR ( "Button 2 pressed" ) );    //  8
  commands.addString ( PSTR ( "Up pressed" ) );          //  9
  commands.addString ( PSTR ( "Down pressed" ) );        // 10 
  commands.addString ( PSTR ( "Left pressed" ) );        // 11 
  commands.addString ( PSTR ( "Right pressed" ) );       // 12 
  
  #ifdef DEBUGIT
  commands.showAll();
  #endif
}
void outputState ( int state )
{
  static int lastState = 0;
  #ifdef DEBUGIT
  if (lastState != state)
    Serial.println ( state );
  lastState = state;  
  #endif
  for (int i=0; i<4; i++)
  {
    digitalWrite (i+8,1);
  }  
  /*
    red   = pin 8;
    green = pin 10
    blue  = pin 11
  */
  switch (state % 4)
  {
    case 1: // serial input received
      digitalWrite (8,0); // red
      break;
      
    case 2:  // login prompt received
      digitalWrite (11,0); // blue
      break;
    
    case 3: // logged in, executing python
      digitalWrite (10,0); // green
      break;
      
    default:
    break;
  }
}

void loop()
{
  char ch;
  int command;
  static bool skipIt = false;
  if (Serial.available())
  {
    ch = Serial.read();
    command = commands.matchString ( ch, false );
    switch (state)
    {
      case 1: 
        if (command == 0) // login: 
        {
          Serial.println ( "pi");
          delay (500);
          Serial.println ( "jukebox");
          delay (500);
          Serial.println ( "cd Desktop");
          delay (500);
          Serial.println ( "python wii_remote_1.py");
          state = 2; // blue 
         }          
     break;
    
      case 2:
        if (command == 1) // Press 1 + 2
        {
          state = 3; // Green
        }
      break;
      
      default: // Pressing some buttons
        if (command > -1) 
        {
          if (skipIt)
            skipIt = false;
          else
          {
            state ++;
            if ((state % 4) == 0)
              state++; // Skip the light off state
            skipIt = true;
          }  
        } 
        break;
              
    }    
  }
  if (millis() > timeout)
  {
    timeout = millis() + 500;
    outputState (state);  
  }  
}
