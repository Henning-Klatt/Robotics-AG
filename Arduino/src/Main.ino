#include <Arduino.h>
#include <SoftwareWire.h>
#include <SPI.h>
#include <Adafruit_MCP3008.h>
#include <Wire.h>
#include "Main.h"

// Open Busses and construct sensor objects
SoftwareWire i2c1(SDA1, SCL1);
Adafruit_MCP3008 adc;

// i2c communication buffers
byte i2cWriteBuffer[0][10];
byte i2cReadBuffer[0][10];

// Global variables used to store sensor values
uint16_t colors[2][4] = { {0, 0, 0, 0}, {0, 0, 0, 0} };
byte light[8] = {0, 0, 0, 0, 0, 0, 0, 0};
byte button = 0;

// read the state of the button into global variable
void readButton() {
    int level = analogRead(BUTTONS);
    if (level > 1010) {
        button = 1;
    } else if (level <= 1010 && level > 995) {
        button = 2;
    } else if (level <= 995 && level > 970) {
        button = 3;
    } else if (level <= 970 && level > 900) {
        button = 4;
    } else {
        button = 0;
    }
}

// transmit the state of the button
void transmitButton() {
    Serial.print("['b',");
    Serial.print(button);
    Serial.print("]");
}

// read the color values into the global array
void readColors() {
    get_Colors(0);
    get_Colors(1);
}

// Transmit the color array in python format
void transmitColors() {
    Serial.print("['c'");
    for (int i = 0; i < 2; i++) { // Different sensors
        Serial.print(",[");
        for (int j = 0; j < 4; j++) { // Different colors values
            Serial.print(colors[i][j]);
            if (j < 3) Serial.print(",");
        }
        Serial.print("]");
    }
    Serial.print("]");
}

void readADC() {
    for (int i = 0; i < 8; i++) {
        light[i] = adc.readADC(i);
    }
}

void transmitADC() {
    Serial.print("['l'");
    for (int i = 0; i < 8; i++) {
        Serial.print(",");
        Serial.print(light[i]);
    }
    Serial.print("]");
}

void serialEvent() {
    while (Serial.available()) {
        char c = (char) Serial.read();
        switch (c) {
            case 'l': // Light sensors
                readADC();
                transmitADC();
                break;
            case 'b': // Button
                readButton();
                transmitButton();
                break;
            case 'c': // Colors
                readColors();
                transmitColors();
        }
    }
}

void setup() {
    Serial.begin(9600);

    // Setup I2C
    i2c0.begin();
    i2c1.begin();

    for (int i = 0; i < 2; i++) {
        init_TCS34725(i);
        get_TCS34725ID(i);         // get the device ID, this is just a test to see if we're connected
    }

    // Setup SPI
    adc.begin(SCK, MOSI, MISO, CS);
}

void loop() {
}

// I2C Communication functions
// ---------------------------------------------------------------------------
/* Send register address and the byte value you want to write the magnetometer and
   loads the destination register with the value you send */
void Writei2cRegisters(byte numberbytes, byte command, byte mode)
{
    byte i = 0;

    if (mode == 0) {
        i2c0.beginTransmission(SensorAddressWrite);   // Send address with Write bit set
        i2c0.write(command);                          // Send command, normally the register address
        for (i=0;i<numberbytes;i++)                       // Send data
            i2c0.write(i2cWriteBuffer[mode][i]);
        i2c0.endTransmission();

        delayMicroseconds(100);      // allow some time for bus to settle
    } else {
        i2c1.beginTransmission(SensorAddressWrite);   // Send address with Write bit set
        i2c1.write(command);                          // Send command, normally the register address
        for (i=0;i<numberbytes;i++)                       // Send data
            i2c1.write(i2cWriteBuffer[mode][i]);
        i2c1.endTransmission();

        delayMicroseconds(100);      // allow some time for bus to settle
    }
}

/* Send register address to this function and it returns byte value
   for the magnetometer register's contents */
byte Readi2cRegisters(int numberbytes, byte command, byte mode)
{
    byte i = 0;

    if (mode == 0) {
        i2c0.beginTransmission(SensorAddressWrite);   // Write address of read to sensor
        i2c0.write(command);
        i2c0.endTransmission();

        delayMicroseconds(100);      // allow some time for bus to settle

        i2c0.requestFrom(SensorAddressRead,numberbytes);   // read data
        for(i=0; i<numberbytes; i++) {
            i2cReadBuffer[mode][i] = i2c0.read();
        }
        i2c0.endTransmission();

        delayMicroseconds(100);      // allow some time for bus to settle
    } else {
        i2c1.beginTransmission(SensorAddressWrite);   // Write address of read to sensor
        i2c1.write(command);
        i2c1.endTransmission();

        delayMicroseconds(100);      // allow some time for bus to settle

        i2c1.requestFrom(SensorAddressRead,numberbytes);   // read data
        for(i=0;i<numberbytes;i++) {
            i2cReadBuffer[mode][i] = i2c1.read();
        }
        i2c1.endTransmission();

        delayMicroseconds(100);      // allow some time for bus to settle
    }
}

void init_TCS34725(byte mode)
{
    i2cWriteBuffer[mode][0] = 0x10;
    Writei2cRegisters(1,ATimeAddress,mode);    // RGBC timing is 256 - contents x 2.4mS =
    i2cWriteBuffer[mode][0] = 0x00;
    Writei2cRegisters(1,ConfigAddress,mode);   // Can be used to change the wait time
    i2cWriteBuffer[mode][0] = 0x00;
    Writei2cRegisters(1,ControlAddress,mode);  // RGBC gain control
    i2cWriteBuffer[mode][0] = 0x03;
    Writei2cRegisters(1,EnableAddress,mode);    // enable ADs and oscillator for sensor
}

void get_TCS34725ID(byte mode)
{
    Readi2cRegisters(1,IDAddress,mode);
    if (i2cReadBuffer[mode][0] = 0x44) {
    } else {
    }
}

/* Reads the register values for clear, red, green, and blue.  */
void get_Colors(byte mode)
{
    Readi2cRegisters(8,ColorAddress,mode);
    colors[mode][3] = (unsigned int)(i2cReadBuffer[mode][1]<<8) + (unsigned int)i2cReadBuffer[mode][0];
    colors[mode][0] = (unsigned int)(i2cReadBuffer[mode][3]<<8) + (unsigned int)i2cReadBuffer[mode][2];
    colors[mode][1] = (unsigned int)(i2cReadBuffer[mode][5]<<8) + (unsigned int)i2cReadBuffer[mode][4];
    colors[mode][2] = (unsigned int)(i2cReadBuffer[mode][7]<<8) + (unsigned int)i2cReadBuffer[mode][6];
}
