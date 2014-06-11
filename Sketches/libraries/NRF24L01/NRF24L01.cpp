#include "nrf24l01.h"
#include <Arduino.h>

//****************************************************
// SPI(nRF24L01) commands
#define RF_READ_REG        0x00  // Define read command to register
#define RF_WRITE_REG       0x20  // Define write command to register
#define RF_RD_RX_PLOAD     0x61  // Define RX payload register address
#define RF_WR_TX_PLOAD     0xA0  // Define TX payload register address
#define RF_FLUSH_TX        0xE1  // Define flush TX register command
#define RF_FLUSH_RX        0xE2  // Define flush RX register command
#define RF_REUSE_TX_PL     0xE3  // Define reuse TX payload register command
#define RF_NOP             0xFF  // Define No Operation, might be used to read status register
//***************************************************
#define RF_RX_DR    0x40
#define RF_TX_DS    0x20
#define RF_MAX_RT   0x10
//***************************************************
// SPI(nRF24L01) registers(addresses)
#define RF_CONFIG          0x00  // 'Config' register address
#define RF_EN_AA           0x01  // 'Enable Auto Acknowledgment' register address
#define RF_EN_RXADDR       0x02  // 'Enabled RX addresses' register address
#define RF_SETUP_AW        0x03  // 'Setup address width' register address
#define RF_SETUP_RETR      0x04  // 'Setup Auto. Retrans' register address
#define RF_CH           0x05  // 'RF channel' register address
#define RF_SETUP        0x06  // 'RF setup' register address
#define RF_STATUS          0x07  // 'Status' register address
#define RF_OBSERVE_TX      0x08  // 'Observe TX' register address
#define RF_CD              0x09  // 'Carrier Detect' register address
#define RF_RX_ADDR_P0      0x0A  // 'RX address pipe0' register address
#define RF_RX_ADDR_P1      0x0B  // 'RX address pipe1' register address
#define RF_RX_ADDR_P2      0x0C  // 'RX address pipe2' register address
#define RF_RX_ADDR_P3      0x0D  // 'RX address pipe3' register address
#define RF_RX_ADDR_P4      0x0E  // 'RX address pipe4' register address
#define RX_ADDR_P5      0x0F  // 'RX address pipe5' register address
#define RF_TX_ADDR         0x10  // 'TX address' register address
#define RF_RX_PW_P0        0x11  // 'RX payload width, pipe0' register address
#define RF_RX_PW_P1        0x12  // 'RX payload width, pipe1' register address
#define RF_RX_PW_P2        0x13  // 'RX payload width, pipe2' register address
#define RF_RX_PW_P3        0x14  // 'RX payload width, pipe3' register address
#define RF_RX_PW_P4        0x15  // 'RX payload width, pipe4' register address
#define RF_RX_PW_P5        0x16  // 'RX payload width, pipe5' register address
#define RF_FIFO_STATUS     0x17  // 'FIFO Status Register' register address

#define RXMODEDELAY 5

static unsigned char RF_TX_ADDRESS[TX_ADR_WIDTH]  = 
{
  0x34,0x43,0x10,0x10,0x01
}; // Define a static TX address

//**************************************************
// NRF24L01 constructor, 
NRF24L01::NRF24L01 (void)
{
  canHear = 0;
  // Initialize the circular receive buffer to empty
  head = 0;
  tail = MAXRECEIVEBUFFER-1;
}
//**************************************************
// function: init_Io 
// Description:
// Initialize io
// flash led one time,chip enable(ready to TX or RX Mode),
// Spi disable,Spi clock line init high
//**************************************************
void NRF24L01::init_io (int channel, bool debug, int csn_pin, int ce_pin)
{
  csnpin = csn_pin;
  cepin = ce_pin;
  pinMode (csnpin,OUTPUT);
  pinMode (cepin,OUTPUT);

  myChannel = channel;
  debugIt = debug;
  
  // Set DDR outputs
  //pinMode (13,OUTPUT);
  //pinMode (11,OUTPUT);  
  SPI_DIR |= ( SCKPIN + MOSIPIN );
  
  // Set DDR input
  //pinMode (12,INPUT);
  SPI_DIR &=~ MISOPIN; // Slave output is an input

  // Set CEPin to 0     
  digitalWrite (cepin, 0);      // Chip enable
  digitalWrite (csnpin,1);      // Spi disable
  SPI_PORT&=~SCKPIN;	        // Spi clock line init high
  
  txTime = 0;
  rxTimeout = 0;
}


bool NRF24L01::RxStringReady ()
{
  bool ready = true;
  int t = tail;
  if ((++t % MAXRECEIVEBUFFER) == head)
    ready = false;
  return ready;
}

char NRF24L01::Read () 
{
  char ch = 0;
  if (RxStringReady())
    ch = receiveBuffer[++tail % MAXRECEIVEBUFFER];
  return ch;	
}

void NRF24L01::RxString ()
{
  unsigned char packetId;
  unsigned char buf[TX_PLOAD_WIDTH] = {0};
  bool debugIt = false;
  
  rxMode();  
  if (rx(buf))
  {
    packetId = buf[0];
	if (debugIt)
	{
      Serial.print ( "[" );
	  Serial.print ( (int) packetId );
	  Serial.println ( "]");
	} 
	
	for (int i=1; i<32; i++)
	{
	  if (buf[i]) 
      { 
	    if (debugIt)
          Serial.print ( (char) buf[i] );		
  	    receiveBuffer[head] = buf[i];
	    head = ++head % MAXRECEIVEBUFFER;
	  }  
  	  else
        break;	
    } 		
    txMode();
	for (int i=1; i<32; i++)
	  buf[i] = 0;
    tx ( buf ); // Send back the ack
  }
}

// Format of packet id byte and 31 data bytes,  last packet has an id byte of -1
// Transmitter will wait for packet acknowledge before sending next packet 
// First 
bool NRF24L01::TxString ( char * msg, int numRetries, unsigned long timeout ) 
{
  int index = 0;
  int len = strlen ( msg );
  char packetId = 0;
  
  unsigned char buf[TX_PLOAD_WIDTH] = {0};
  unsigned char rxBuf[TX_PLOAD_WIDTH];
  unsigned long timeExpires;
  bool ok = false;
  
  while (numRetries-- && !ok)
  {
    Serial.print ( "Transmission: " );
	Serial.println (numRetries); 
    while (len)
    {
      txMode();
      for (int i=0; i<32; i++)
	    buf[i] = 0;
	  
      Serial.print ( "len: " );
  	  Serial.println ( len );
      if (len > 31) 
	  {
	    buf[0] = packetId++ % 128;
	    for (int i=1; i<32; i++)
	    {
	      buf[i] = msg[index++];
	    } 	
        len = strlen ( &msg[index]);	  
  	  }
	  else
	  {
	    buf[0] = -1;
	    for (int i=0; i<len; i++)
	      buf[i+1] = msg[index++];
	    len = 0;	
	  }
	  delay (150); // Must be longer than rx delay
	  tx (buf);
	  // Wait for response.
	  rxMode();
	
	  // Wait 2 seconds for an acknowledgement
	  timeExpires = millis() + timeout;
	  while (millis() <= timeExpires)
	  { 
	    if (rx(rxBuf))
        {
	      Serial.print ( "ack:[" );
		  Serial.print ((int) rxBuf[0]);
		  Serial.println ( "]");
		  ok = true;
		  
          //SPI_RW_Reg(RF_FLUSH_TX,0); // Flush the tx register
	      break;
        }	  
	  }
	
  	  if (millis() > timeExpires)
	  {
	    Serial.println ( "Never got an acknowledgement in 2 seconds");
		ok = false;
	    break;
	  }
	}  
  }
  
  return ok;  
}

void NRF24L01::IsHeard ( int index, bool wasHeard )
{
  if ((index >= 0) && (index <8)) 
    if (wasHeard) // Set bits
	  canHear |= 1 << index; 
	else // Clear
	  canHear &= ~(1 << index);
}

void NRF24L01::rxModeNoDelay (void)
{
  digitalWrite (cepin,0);
  SPI_Write_Buf(RF_WRITE_REG + RF_RX_ADDR_P0, RF_TX_ADDRESS, TX_ADR_WIDTH); // Use the same address on the RX device as the TX device
  SPI_RW_Reg(RF_WRITE_REG + RF_EN_AA, 0x01);                             // Enable Auto.Ack:Pipe0
  SPI_RW_Reg(RF_WRITE_REG + RF_EN_RXADDR, 0x01);                         // Enable Pipe0
  SPI_RW_Reg(RF_WRITE_REG + RF_CH, myChannel);                        // Select RF channel
  SPI_RW_Reg(RF_WRITE_REG + RF_RX_PW_P0, TX_PLOAD_WIDTH);                // Select same RX payload width as TX Payload width
  SPI_RW_Reg(RF_WRITE_REG + RF_SETUP, 0x06); // was 0x6, 7, max power?        // TX_PWR:0dBm, Datarate:2Mbps, LNA:HCURR
  SPI_RW_Reg(RF_WRITE_REG + RF_CONFIG, 0x0f);                            // Set PWR_UP bit, enable CRC(2 unsigned chars) & Prim:RX. RX_DR enabled..
  digitalWrite (cepin,1);
  modeIsTransmit = false;
}
/**************************************************
 * Function: rxMode();
 * 
 * Description:
 * This function initializes one nRF24L01 device to
 * RX Mode, set RX address, writes RX payload width,
 * select RF channel, datarate & LNA HCURR.
 * After init, CE is toggled high, which means that
 * this device is now ready to receive a datapacket.
/**************************************************/
void NRF24L01::rxMode(void)
{
  delay (RXMODEDELAY);
  rxModeNoDelay(); 
  //unsigned char status=SPI_Read(STATUS);
  delay (RXMODEDELAY);
  //  This device is now ready to receive one packet of 16 unsigned chars payload from a TX device sending to address
  //  '3443101001', with auto acknowledgment, retransmit count of 10, RF channel 40 and datarate = 2Mbps.
  txTime = 0;
}

/**************************************************
 * Function: txMode();
 * 
 * Description:
 * This function initializes one nRF24L01 device to
 * TX mode, set TX address, set RX address for auto.ack,
 * fill TX payload, select RF channel, datarate & TX pwr.
 * PWR_UP is set, CRC(2 unsigned chars) is enabled, & PRIM:TX.
 * 
 * ToDo: One high pulse(>10us) on CE will now send this
 * packet and expect an acknowledgment from the RX device.
 **************************************************/
void NRF24L01::txMode(void)
{

  delay (RXMODEDELAY + RXMODEDELAY);
  digitalWrite (cepin,0); 
  SPI_Write_Buf(RF_WRITE_REG + RF_TX_ADDR, RF_TX_ADDRESS, TX_ADR_WIDTH);    // Writes TX_Address to nRF24L01
  SPI_Write_Buf(RF_WRITE_REG + RF_RX_ADDR_P0, RF_TX_ADDRESS, TX_ADR_WIDTH); // RX_Addr0 same as TX_Adr for Auto.Ack
  SPI_RW_Reg(RF_WRITE_REG + RF_EN_AA, 0x01);                             // Enable Auto.Ack:Pipe0
  SPI_RW_Reg(RF_WRITE_REG + RF_EN_RXADDR, 0x01);                         // Enable Pipe0
  SPI_RW_Reg(RF_WRITE_REG + RF_SETUP_RETR, 0x1a);                        // 500us + 86us, 10 retrans...
  SPI_RW_Reg(RF_WRITE_REG + RF_CH, myChannel);                           // Select RF channel 40
  SPI_RW_Reg(RF_WRITE_REG + RF_SETUP, 0x06);  // was 0x06                            // Was 7. Max Power?  // TX_PWR:0dBm, Datarate:2Mbps, LNA:HCURR
  SPI_RW_Reg(RF_WRITE_REG + RF_CONFIG, 0x0e);                            // Set PWR_UP bit, enable CRC(2 unsigned chars) & Prim:TX. MAX_RT & TX_DS enabled..

  digitalWrite (cepin,1);
  modeIsTransmit = true;
  delay (RXMODEDELAY + RXMODEDELAY);
  rxTimeout = 0;
}


/*
  Poll receiver 
  return true if status indicates a receive buffer is ready
*/
bool NRF24L01::rx ( unsigned char * buf )
{
  bool rxReady = false;     
  unsigned char status=SPI_Read(RF_STATUS);
        
  if (status&RF_RX_DR)                                    // if receive data ready (TX_DS) interrupt
  {
    SPI_Read_Buf(RF_RD_RX_PLOAD, buf, TX_PLOAD_WIDTH);    // read playload to rx_buf
    SPI_RW_Reg(RF_FLUSH_RX,0);                            // clear RX_FIFO
    SPI_RW_Reg(RF_WRITE_REG+RF_STATUS,status);               // clear RX_DR or TX_DS or MAX_RT interrupt flag
    rxReady = true;      
  }
  if (rxReady && debugIt)
  {
    Serial.print ( "rx: [" );
    Serial.print ( (char) (buf[0] + '0') );
    Serial.print ( "," );
    Serial.print ( (char) (buf[1] + '0') );
    Serial.print ( "," );
    Serial.print ( (char) (buf[2] + '0') );
    Serial.print ( "," );
    Serial.print ( (char) (buf[3] + '0') );
    Serial.print ( "," );
    Serial.print ( buf[4] );
    Serial.print ( "," );
    Serial.print ( buf[5] );
    Serial.print ( "," );
    if (buf[5] < 32) // Data
      Serial.print ((char) (buf[5] + '0')); 
    else
      Serial.print ( (char) buf[5] );

    Serial.println ( "]" );
  }
  return rxReady;
}

/* transmit a 32 byte buffer */
void NRF24L01::tx ( unsigned char * buf ) 
{

  unsigned char status = SPI_Read(RF_STATUS);         // read register STATUS's value
  SPI_RW_Reg(RF_FLUSH_TX,0);                                  
  SPI_Write_Buf(RF_WR_TX_PLOAD,buf,TX_PLOAD_WIDTH);   // write playload to TX_FIFO
  delay (10);
  if(status&RF_MAX_RT)                                // if receive data ready (MAX_RT) interrupt, this is retransmit than  SETUP_RETR                          
  {
    SPI_RW_Reg(RF_FLUSH_TX,0);
    SPI_Write_Buf(RF_WR_TX_PLOAD,buf,TX_PLOAD_WIDTH); // disable standy-mode
  }
  SPI_RW_Reg(RF_WRITE_REG+RF_STATUS,status);          // clear RX_DR or TX_DS or MAX_RT interrupt flag
}


/**************************************************
 * Function: SPI_RW();
 * 
 * Description:
 * Writes one unsigned char to nRF24L01, and return the unsigned char read
 * from nRF24L01 during write, according to SPI protocol
 **************************************************/
unsigned char NRF24L01::SPI_RW(unsigned char Byte)
{
  unsigned char i;
  for(i=0;i<8;i++)                      // output 8-bit
  {
    if(Byte&0x80)
    {
      SPI_PORT |=MOSIPIN;    // output 'unsigned char', MSB to MOSI
    }
    else
    {
      SPI_PORT &=~MOSIPIN;
    }
    SPI_PORT|=SCKPIN;                      // Set SCK high..
    Byte <<= 1;                         // shift next bit into MSB..
    if(SPI_IN & MISOPIN)
    {
      Byte |= 1;       	        // capture current MISO bit
    }
    SPI_PORT&=~SCKPIN;            	        // ..then set SCK low again
  }
  return(Byte);           	        // return read unsigned char
}
/**************************************************/

/**************************************************
 * Function: SPI_RW_Reg();
 * 
 * Description:
 * Writes value 'value' to register 'reg'
/**************************************************/
unsigned char NRF24L01::SPI_RW_Reg(unsigned char reg, unsigned char value)
{
  unsigned char status;

  digitalWrite (csnpin, 0);              //CSN low, init SPI transaction 
  status = SPI_RW(reg);             // select register
  SPI_RW(value);                    // ..and write value to it..
  digitalWrite (csnpin, 1);              // CSN high again to disable 

  return(status);                   // return nRF24L01 status unsigned char
}
/**************************************************/

/**************************************************
 * Function: SPI_Read();
 * 
 * Description:
 * Read one unsigned char from nRF24L01 register, 'reg'
/**************************************************/
unsigned char NRF24L01::SPI_Read(unsigned char reg)
{
  unsigned char reg_val;

  digitalWrite (csnpin, 0);             //CSN low, initialize SPI comm
  SPI_RW(reg);                   // Select register to read from..
  reg_val = SPI_RW(0);           // ..then read register value
  digitalWrite (csnpin, 1);         //CSN high, terminate SPI communication
  return(reg_val);               // return register value
}
/**************************************************/

/**************************************************
 * Function: SPI_Read_Buf();
 * 
 * Description:
 * Reads 'unsigned chars' #of unsigned chars from register 'reg'
 * Typically used to read RX payload, Rx/Tx address
/**************************************************/
unsigned char NRF24L01::SPI_Read_Buf(unsigned char reg, unsigned char *pBuf, unsigned char bytes)
{
  unsigned char status,i;

  digitalWrite (csnpin, 0);                //Set CSN low, init SPI transaction 
  status = SPI_RW(reg);       	    // Select register to write to and read status unsigned char

  for(i=0;i<bytes;i++)
  {
    pBuf[i] = SPI_RW(0);    // Perform SPI_RW to read unsigned char from nRF24L01
  }

  digitalWrite (csnpin,1);      //Set CSN high again
  return(status);                  // return nRF24L01 status unsigned char
}
/**************************************************/

/**************************************************
 * Function: SPI_Write_Buf();
 * 
 * Description:
 * Writes contents of buffer '*pBuf' to nRF24L01
 * Typically used to write TX payload, Rx/Tx address
/**************************************************/
unsigned char NRF24L01::SPI_Write_Buf(unsigned char reg, unsigned char *pBuf, unsigned char bytes)
{
  unsigned char status,i;

  digitalWrite (csnpin, 0);            //Set CSN low, init SPI transaction
  status = SPI_RW(reg);             // Select register to write to and read status unsigned char
  for(i=0;i<bytes; i++)             // then write all unsigned char in buffer(*pBuf)
  {
    SPI_RW(*pBuf++);
  }
  digitalWrite (csnpin, 1);        // Set CSN high again
  return(status);                  // return nRF24L01 status unsigned char
}
