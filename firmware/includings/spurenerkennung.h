#pragma config(Sensor, S1,     colorSensorLeft, sensorI2CCustom)#pragma config(Sensor, S2,     colorSensorMiddle, sensorLightActive)#pragma config(Sensor, S3,     colorSensorRight, sensorI2CCustom)#include "drivers/hitechnic-colour-v2.h"#include "includings/variablen.h"#include "includings/move.h"int Leftred, Leftgreen, Leftblue; //RGB Werte Sensor Linksint Rightred, Rightgreen, Rightblue; //RGB Werte Sensor rechtsvoid RefreshColor(){ HTCS2readRGB(colorSensorLeft, Leftred, Leftgreen, Leftblue); //Linker RGB Sensor auslesen HTCS2readRGB(colorSensorRight, Rightred, Rightgreen, Rightblue); //Rechter RGB Sensor auslesen if(Leftred < 100) LeftLine = COLOR_BLACK; //Wenn ROT Links Spur vorhanden else LeftLine = COLOR_WHITE; //Ansonsten keine Spur if(Rightred < 100) RightLine = COLOR_BLACK; //Wenn ROT Rechts Spur vorhanden else RightLine = COLOR_WHITE; //Ansonsten keine Spur if(SensorValue(colorSensorMiddle) <= 50) MiddleLine = COLOR_BLACK; else MiddleLine = COLOR_WHITE; nxtDisplayBigTextLine(1, "%d", LeftLine); nxtDisplayBigTextLine(3, "%d", MiddleLine); nxtDisplayBigTextLine(5, "%d", RightLine);}void FollowLine(const int speed){ //____________By_Markus_Manz_____________// if(MiddleLine == COLOR_BLACK && RightLine == COLOR_WHITE && LeftLine == COLOR_WHITE){  move(speed, speed, 0, 0); } if(LeftLine == COLOR_BLACK && MiddleLine != COLOR_BLACK){  move(speed, -(speed), 50, 0); } if(RightLine == COLOR_BLACK && MiddleLine != COLOR_BLACK){  move(-(speed), speed, 50, 0); } //________NICHT MEHR BY Markus_Manz___________// if(RightLine == COLOR_BLACK && MiddleLine == COLOR_BLACK) {  move(speed, speed, 100, 0);  RefreshColor();    while(RightLine == COLOR_WHITE && MiddleLine == COLOR_WHITE && LeftLine == COLOR_BLACK) {   move(-speed, 0, 5, 0);   move(0, speed, 1, 0);   RefreshColor();  }   move(-speed, 0, 70, 0); } if(LeftLine == COLOR_BLACK && MiddleLine == COLOR_BLACK) {  move(speed, speed, 100, 0);  RefreshColor();    while(LeftLine == COLOR_WHITE && MiddleLine == COLOR_WHITE && RightLine == COLOR_WHITE) {   move(0, -speed, 5, 0);   move(speed, 0, 1, 0);   RefreshColor();  }   move(0, -speed, 70, 0); }   if(LeftLine == COLOR_BLACK && RightLine == COLOR_BLACK && MiddleLine == COLOR_BLACK){  move(-speed, -speed, 100, 0); }if(LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && MiddleLine == COLOR_WHITE) {  move(speed, speed, 0, 0); }}
