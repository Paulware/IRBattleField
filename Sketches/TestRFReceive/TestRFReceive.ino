#include <NRF24L01.h>

NRF24L01 rf;
unsigned char rx_buf[TX_PLOAD_WIDTH];
void setup () 
{
  rf.init_io(40,false,18,8);   // Initialize IO port
  rf.rxMode();
  Serial.begin (115200);
  Serial.println ( "Rx Tester ready");

}
void loop () 
{
  char ch;
  // Check for rf transmission
  if (rf.rx (rx_buf))
  {
    ch = rx_buf[0];
    switch (ch )
    {
      case 'F':
      case 'L':
      case 'B':
      case 'G':
      case 'R':
      case 't':
      case 'T':
      case 'A':
      Serial.print (ch);
      break;
      
      default:
        // if (ch) 
          Serial.print (ch, DEC);
        break;
    }
  }

}
