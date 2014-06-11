#include <math.h>
#include <NRF24L01.h>

// Radio constants
#define TXDELAY 1

// Datasheet of thermistor will specify following values:
#define BCONSTANT 4050.0f
#define T0 298.15f
#define R0 10000.0f

// '0': Master, '1': First Slave, '2': Second Slave, etc
#define MYUNITNUMBER '1'

// Transmit Channel
#define CHANNEL 41

unsigned char rx_buf[TX_PLOAD_WIDTH] = {0}; // initialize value
unsigned char tx_buf[TX_PLOAD_WIDTH] = {0};

unsigned long checkTemp = 0;

NRF24L01 rf;

//***************************************************
void setup() 
{
  rf.init_io(CHANNEL, false);   // Initialize IO port

  Serial.begin(115200);
  Serial.println ( "Slave here" );
  rf.rxMode();
  checkTemp = millis();
}
unsigned char c = 'S'; // Startup indicator
unsigned char lastC = ' ';
unsigned char lastStatus = 0;

byte state;
/*
   Handle a received character
   
   Global Variables:
     state: For processing the received string.
*/
void processCh (char ch, int index ) 
{
  if (ch)
  {
    if (index == 0) // first character
      state = 0;
      
    switch (state)
    {
      case 0: // first character
        state = 1;        
        if (ch == MYUNITNUMBER) 
        {
          rf.txMode();
        }
        else
          Serial.print ( ch );
        break;
      default:
        Serial.print ( ch );
        break;  
    }
  }  
}

byte Temperature(int AnalogInputNumber)
 {
   float R,T;
   float R_Balance = 10000.0f; // Balance Resistor (same resistance as R0 of thermistor)

   R=1024.0f*R_Balance/float(analogRead(AnalogInputNumber))-R_Balance;
   T=1.0f/(1.0f/T0+(1.0f/BCONSTANT)*log(R/R0));
   // Determine Fahrenheit temperature 
   T=9.0f*(T-273.15f)/5.0f+32.0f;
   byte value = (byte) T;
 
  return T;
 }

byte getData ( ) 
{
  int fahrenheit;
  byte value = 0;
  switch (MYUNITNUMBER)
  {
    case '1': // Thermistor 
    value = Temperature (0);
    default:
    break;
  }
  
  return value;
}

void loop() 
{  
  unsigned char status;
    
  for(;;)
  {
    if (checkTemp)
    {
      if (millis() > checkTemp)
      {
        checkTemp = millis() + 1000;
      }
    }
    if (rf.modeIsTransmit) 
    {       
      if (rf.txTime) // Master requests data from slave
      {
        if (millis() > rf.txTime)
        {
          /* 
              Format of tx data bytes: 
              Destination | Source | Command | Data 
          */
          for(int i=0; i<32; i++)
            tx_buf[i] = 0;        
          
          tx_buf[0] = '1';                             // Request data from slave device '1' 
          tx_buf[1] = MYUNITNUMBER;                    // Source
          tx_buf[2] = '?';                             // Command 

          rf.tx ( tx_buf );                              // Transmit data
          
          rf.rxMode();                              
          rf.rxTimeout = millis() + 1000;    // Timeout if response not received in 1 second
        }
      }
      
      if (rf.txTime) // Slave is going to transmit data?
      {
        if (millis() > rf.txTime) 
        {
          for(int i=0; i<32; i++)
            tx_buf[i] = 0;        
          tx_buf[0] = '0';          // Always respond to master 
          tx_buf[1] = MYUNITNUMBER; // Source
          tx_buf[2] = '!';          // Command           
          tx_buf[3] = getData();    // Always followed by a data value 
          Serial.print ( "Slave responding with data: " );
          Serial.println ( getData());
          
          rf.tx (tx_buf);
          rf.rxMode();
        }  
      }
    }
    else // Receive Mode 
    {
      if (rf.rx (rx_buf))
      {
        if (rx_buf[0] == MYUNITNUMBER)
        {
          // Wait to allow master to transition into receive mode 
          rf.txTime = millis() + 100; 
          rf.txMode(); // Go to tx mode to respond with my data
        }  
      }      
    }  
  }  
}
