#pragma config(Motor, motorA, left, tmotorNXT, PIDControl, encoder)
#pragma config(Motor, motorB, right, tmotorNXT, PIDControl, encoder)

#include "includings/spurenerkennung.h"

task main()
{
	while(true) {
		RefreshColor();
		nxtDisplayBigTextLine(1, "L: %d", LeftLine);
		nxtDisplayBigTextLine(3, "M: %d", MiddleLine);
		nxtDisplayBigTextLine(5, "R: %d", RightLine);


		if(MiddleLine == 1){
			//Vorwaerts
			motor [ left ] = 100;
			motor [ right ] = 100;
		}



	}
}
