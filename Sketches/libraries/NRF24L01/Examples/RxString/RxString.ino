#include <NRF24L01.h>
#define CHANNEL 40

NRF24L01 rf;

void setup ()
{
  
  Serial.begin (115200);
  Serial.println ("NRF24L01 receiver ready" );

  // rf initialization
  rf.init_io(CHANNEL,false);   // Initialize IO port
  
  if (rf.RxStringReady())
    Serial.println ( "On power up, receiver is ready" );
  else
    Serial.println ( "On power up, receiver is not ready" );
}

void loop()
{
  rf.RxString();
  while (rf.RxStringReady())
    Serial.print ( rf.Read());
  
}
