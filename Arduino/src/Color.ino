#include <Arduino.h>
#include <Wire.h>
#include <SoftwareWire.h>
#include "Main.h"
#include "Color.h"
// I2C Color Sensors
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
void Readi2cRegisters(int numberbytes, byte command, byte mode)
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
    // XXX: dafuq
   /* if (i2cReadBuffer[mode][0] = 0x44) { */
    /* } else { */
    /* } */
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
