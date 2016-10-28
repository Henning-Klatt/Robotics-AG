#pragma config(Motor, motorA, left, tmotorNXT, PIDControl, encoder)
#pragma config(Motor, motorB, right, tmotorNXT, PIDControl, encoder)

#include "includings/spurenerkennung.h"

task main()
{
	while(true) {
		RefreshColor();
		nxtDisplayBigTextLine(1, "L: %d", LeftColor;
		nxtDisplayBigTextLine(3, "M: %d", MiddleColor);
		nxtDisplayBigTextLine(5, "R: %d", RightColor);


		if(MiddleLine == 1){
			//Vorwaerts
			motor [ left ] = 100;
			motor [ right ] = 100;
		}



	}
}
