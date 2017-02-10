#include "drivers/hitechnic-colour-v2.h"
#include "includings/variablen.h"

void RefreshColor()
{
	int Leftred, Leftgreen, Leftblue; //RGB Werte Sensor Links
	int Rightred, Rightgreen, Rightblue; //RGB Werte Sensor rechts

	HTCS2readRGB(colorSensorLeft, Leftred, Leftgreen, Leftblue); //Linker RGB Sensor auslesen
	HTCS2readRGB(colorSensorRight, Rightred, Rightgreen, Rightblue); //Rechter RGB Sensor auslesen
	int colorl = HTCS2readColor(colorSensorLeft);
	int colorr = HTCS2readColor(colorSensorRight);

	if (HTCS2readColor(colorSensorLeft) == 4) LeftLine = COLOR_GREEN;
	else if(Leftred < 100) LeftLine = COLOR_BLACK; //Wenn ROT Links Spur vorhanden
	else LeftLine = COLOR_WHITE; //Ansonsten keine Spur

	if (HTCS2readColor(colorSensorRight) == 4) RightLine = COLOR_GREEN;
	else if(Rightred < 100) RightLine = COLOR_BLACK; //Wenn ROT Rechts Spur vorhanden
	else RightLine = COLOR_WHITE; //Ansonsten keine Spur


	if(SensorValue(colorSensorMiddle) <= 50) MiddleLine = COLOR_BLACK;
	else MiddleLine = COLOR_WHITE;
}
