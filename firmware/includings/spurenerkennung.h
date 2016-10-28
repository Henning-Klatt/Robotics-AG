#pragma config(Sensor, S1,     colorSensorLeft, sensorI2CCustom)
#pragma config(Sensor, S2,     colorSensorMiddle, sensorLightActive)
#pragma config(Sensor, S3,     colorSensorRight, sensorI2CCustom)

#include "drivers/hitechnic-colour-v2.h"
#include "includings/variablen.h"

void RefreshColor()
{
	(HTCS2readRGB(colorSensorLeft, Leftred, Leftgreen, Leftblue)); //Linker RGB Sensor auslesen
	(HTCS2readRGB(colorSensorRight, Rightred, Rightgreen, Rightblue)); //Rechter RGB Sensor auslesen

	if(Leftred < 100) LeftLine = 1; //Wenn ROT Links Spur vorhanden
	else LeftLine = 0; //Ansonsten keine Spur

	if(Rightred < 100) RightLine = 1; //Wenn ROT Rechts Spur vorhanden
	else RightLine = 0; //Ansonsten keine Spur


	if(SensorValue(colorSensorMiddle) <= 50) MiddleLine = 0;
	else MiddleLine = 0;

}
