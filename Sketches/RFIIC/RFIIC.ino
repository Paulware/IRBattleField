#include <NRF24L01.h>

NRF24L01 rf;
unsigned char buf[TX_PLOAD_WIDTH];
bool receiving = true;
void setup () 
{
  // Note: 16 is a change from all schematics.
  // This is because 18 is necessary for SDA
  rf.init_io(40,false,16,8);   // Initialize IO port
  rf.rxMode();
  
  Serial.begin (115200);
  Serial.println ( "Receiving...Enter text to transmit");
}

void loop () 
{
  char ch;  
  if (Serial.available()) // The user is typing something
  {
    if (receiving)
      rf.txMode();
    ch = Serial.read();
    if (ch >=' ')
    {
      buf[0] = ch;
      rf.tx (buf);
      receiving = false; 
      delay (1); // necessary?
    }  
    else if (ch == 13)
      Serial.println ( "Text transmitted" );
  }
  
  // Check for rf transmission
  if (receiving)
    if (rf.rx (buf))
    {
      ch = buf[0];
      Serial.print (ch);
    }
}
