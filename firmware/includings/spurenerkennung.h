#pragma config(Sensor, S1,     colorSensorLeft, sensorI2CCustom)
#pragma config(Sensor, S2,     colorSensorMiddle, sensorLightActive)
#pragma config(Sensor, S3,     colorSensorRight, sensorI2CCustom)

#include "drivers/hitechnic-colour-v2.h"
#include "includings/variablen.h"

void RefreshColor()
{
	int Leftred, Leftgreen, Leftblue;
	int Rightred, Rightgreen, Rightblue;


	(HTCS2readRGB(colorSensorLeft, Leftred, Leftgreen, Leftblue)); //Linker RGB Sensor auslesen
	(HTCS2readRGB(colorSensorRight, Rightred, Rightgreen, Rightblue)); //Rechter RGB Sensor auslesen

	if(Leftred < 100) LeftLine = COLOR_BLACK; //Wenn ROT Links schwarz
	else LeftColor = COLOR_WHITE; //Ansonste weiss

	if(Rightred < 100) RightLine = COLOR_BLACK; //Wenn ROT Rechts schwarz
	else RightColor = COLOR_WHITE; //Ansonsten weiss


	if(SensorValue(colorSensorMiddle) <= 50) MiddleLine = COLOR_BLACK;
	else MiddleColor = COLOR_WHITE;

}
