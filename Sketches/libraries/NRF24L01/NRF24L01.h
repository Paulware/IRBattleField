// nRF24L01.h
#ifndef NRF24L01_h
#define NRF24L01_h

//*********************************************
#define SPI_PORT PORTB
#define SPI_DIR  DDRB
#define SPI_IN   PINB
//---------------------------------------------
#define TX_ADR_WIDTH    5   
// 5 unsigned chars TX(RX) address width
#define TX_PLOAD_WIDTH  1  
// 20 unsigned chars TX payload
//---------------------------------------------
#define SCKPIN      0x20
// SCK BIT:  Digital Input     SPI Clock
// SCK = D13
#define MISOPIN     0x10
// MISO BIT: Digital Output    SPI Slave Data Output, with tri-state option\
// MISO = D12
//#define CSNPIN      0x04
#define MOSIPIN     0x08
// MOSI BIT: Digital Input     SPI Slave Data Input
// MOSI = D11 
// #define IRQPIN      0x20
// IRQ BIT:  Digital Output    Maskable interrupt pin
//*********************************************
#define TX_ADR_WIDTH    5   // 5 unsigned chars TX(RX) address width
#define TX_PLOAD_WIDTH  32  // 32 unsigned chars TX payload

class NRF24L01 {
public:

  unsigned long txTime;
  unsigned long rxTimeout;
  bool modeIsTransmit;
  unsigned char canHear;

  /* Constructor */  
  NRF24L01 (void);

  /* Record if a transmitter was heard */
  void IsHeard ( int index, bool wasHeard );

  //**************************************************
  // Function: init_io();
  // Description:
  // flash led one time,chip enable(ready to TX or RX Mode),
  // Spi disable,Spi clock line init high
  //**************************************************
  void init_io(int channel, bool debug, int csn_pin, int ce_pin);  
  /*
    Poll receiver 
    return true if the first byte received == MYUNITNUMBER 
  */
  bool rx ( unsigned char * buf );
  
  /* transmit a 32 byte buffer */
  void tx ( unsigned char * buf ); 
  
  /* transmit a String of X bytes */
  bool TxString ( char * msg, int numRetries, unsigned long timeout );
  
  /* receive a string of X bytes, note: circular receive buffer is 255 characters */
  void RxString ();

  bool RxStringReady ();
  char Read ();
  
  
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
   * packet and expext an acknowledgment from the RX device.
   **************************************************/
  void txMode(void);
  
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
  void rxMode(void); 
  void rxModeNoDelay(void); 

  private:
  
  int csnpin;
  int cepin;
  
  // Circular receive buffer
  int head;
  int tail;
  #define MAXRECEIVEBUFFER 255
  unsigned char receiveBuffer[MAXRECEIVEBUFFER];
  
  // Channel set by call to init_io
  int myChannel; 
  
  // Set by user to show receive string
  bool debugIt;
  
  
  
  /**************************************************
   * Function: SPI_Write_Buf();
   * 
   * Description:
   * Writes contents of buffer '*pBuf' to nRF24L01
   * Typically used to write TX payload, Rx/Tx address
  /**************************************************/
  unsigned char SPI_Write_Buf(unsigned char reg, 
             unsigned char *pBuf, unsigned char bytes);
  /**************************************************
   * Function: SPI_Read_Buf();
   * 
   * Description:
   * Reads 'unsigned chars' #of unsigned chars from register 'reg'
   * Typically used to read RX payload, Rx/Tx address
  /**************************************************/
  unsigned char SPI_Read_Buf(unsigned char reg, 
            unsigned char *pBuf, unsigned char bytes);  
            
  /**************************************************
   * Function: SPI_Read();
   * 
   * Description:
   * Read one unsigned char from nRF24L01 register, 'reg'
  /**************************************************/
  unsigned char SPI_Read(unsigned char reg);  

  /**************************************************
   * Function: SPI_RW_Reg();
   * 
   * Description:
   * Writes value 'value' to register 'reg'
  /**************************************************/
  unsigned char SPI_RW_Reg(unsigned char reg, unsigned char value);

  /**************************************************
   * Function: SPI_RW();
   * 
   * Description:
   * Writes one unsigned char to nRF24L01, and return the unsigned char read
   * from nRF24L01 during write, according to SPI protocol
   **************************************************/
  unsigned char SPI_RW(unsigned char Byte);

};
#endif
