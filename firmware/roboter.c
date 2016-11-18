#pragma config(Sensor, S1,     colorSensorLeft, sensorI2CCustom)
#pragma config(Sensor, S2,     colorSensorMiddle, sensorLightActive)
#pragma config(Sensor, S3,     colorSensorRight, sensorI2CCustom)
#pragma config(Motor,  motorA,          left,          tmotorNXT, PIDControl, encoder)
#pragma config(Motor,  motorB,          right,         tmotorNXT, PIDControl, encoder)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

#include "includings/spurenerkennung.h"
#include "includings/variablen.h"
#include "includings/move.h"

task main()
{
	motor[motorA] = 100;
	motor[motorB] = 100;
	wait10Msec(100);
	while(true) {
		RefreshColor();
		FollowLine(50);
	}
}
