#ifndef MAIN_H_

#define SCL0 A5
#define SDA0 A4
#define i2c0 Wire //Make Software and Hardware i2c consistent

#define SCL1 3
#define SDA1 4

#define COLOR_ADDR 0x29

#define SENSOR_LED 2
#define BUTTONS A0
#define BUZZER 5

#define SCK 10
#define MISO 11
#define MOSI 12
#define CS 13

// Color sensor constants
#define SensorAddressWrite 0x29 //
#define SensorAddressRead 0x29 // 
#define EnableAddress 0xa0 // register address + command bits
#define ATimeAddress 0xa1 // register address + command bits
#define WTimeAddress 0xa3 // register address + command bits
#define ConfigAddress 0xad // register address + command bits
#define ControlAddress 0xaf // register address + command bits
#define IDAddress 0xb2 // register address + command bits
#define ColorAddress 0xb4 // register address + command bits

#endif
