#include <Arduino.h>
#include <SoftwareWire.h>
#include <SPI.h>
#include <Adafruit_MCP3008.h>
#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>
#include "Main.h"

// Open Busses and construct sensor objects
SoftwareWire i2c1(SDA1, SCL1);
Adafruit_MCP3008 adc;
MPU6050 accelgyro;

// i2c communication buffers
byte i2cWriteBuffer[0][10];
byte i2cReadBuffer[0][10];

// Global variables used to store sensor values
uint16_t colors[2][4] = { {0, 0, 0, 0}, {0, 0, 0, 0} };
int16_t gyro[3] = {0, 0, 0};
int16_t accel[3] = {0, 0, 0};
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

void readGyro() {
    accelgyro.getMotion6(&accel[0], &accel[1], &accel[2], &gyro[0], &gyro[1], &gyro[2]);
}

void transmitGyro() {
    Serial.print("['a'");
    for (int i = 0; i < 3; i++) {
        Serial.print(",");
        Serial.print(accel[i]);
    }
    Serial.print(",g");
    for (int i = 0; i < 3; i++) {
        Serial.print(",");
        Serial.print(gyro[i]);
    }
    Serial.print("]");
}

void serialEvent() {
    while (Serial.available()) {
        char c = (char) Serial.read();
        Serial.print(c);
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
            case 'g':
                readGyro();
                transmitGyro();
        }
    }
}

void setup() {
    Serial.begin(9600);

    // Setup I2C
    i2c0.begin();
    i2c1.begin();

    // Setup color sensors
    for (int i = 0; i < 2; i++) {
        init_TCS34725(i);
        get_TCS34725ID(i);         // get the device ID, this is just a test to see if we're connected
    }
    accelgyro.initialize();

    // Setup SPI
    adc.begin(SCK, MOSI, MISO, CS);
}

void loop() {
}

