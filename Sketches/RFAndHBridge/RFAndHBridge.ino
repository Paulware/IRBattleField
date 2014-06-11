#include <NRF24L01.h>

NRF24L01 rf;
unsigned char rx_buf[TX_PLOAD_WIDTH];
void setup () 
{
  int hPins[] = {5,6,9,10};
  rf.init_io(40,false,18,8);   // Initialize IO port
  rf.rxMode();
  Serial.begin (115200);
  Serial.println ( "Rx Tester ready");
  for (int i=0; i<4; i++)
  {
    pinMode (hPins[i],OUTPUT);
	digitalWrite (hPins[i],0);
  }
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
      break;
      case 'B':
	    digitalWrite (5,0);
		digitalWrite (9,0);
		digitalWrite (6,1);
		digitalWrite (10,1);
        Serial.print (ch);
 	  break;
      case 'G':
	    digitalWrite (6,0);
		digitalWrite (10,0);
		digitalWrite (5,1);
		digitalWrite (9,1);
        Serial.print (ch);
        break;	  
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
