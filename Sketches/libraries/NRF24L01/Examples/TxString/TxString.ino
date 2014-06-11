#include <NRF24L01.h>
#define CHANNEL 40

NRF24L01 rf;

void setup ()
{
  Serial.begin (115200);

  // rf initialization
  rf.init_io(CHANNEL,false);   // Initialize IO port
  if (rf.TxString ( "Hello World what is going on?  That is all Blah Blah Blah", 5, 5000 ))
    Serial.println ( "It all transmitted ok" );
  else
    Serial.println ( "It did not transmit successfully" );  
}

void loop()
{
}
