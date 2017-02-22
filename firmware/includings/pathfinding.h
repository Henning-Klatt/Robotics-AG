#include "includings/move.h"
#include "includings/pathfinding/rotate.h"
#include "includings/pathfinding/findline.h"

void PathFinder(const int speed){
	nxtDisplayClearTextLine(1);
	nxtDisplayClearTextLine(3);
	nxtDisplayString(1, "FollowLine");
	nxtDisplayString(3, "Speed: %d", speed);
	/*----------------------------------------------------------------------------------------------------------------*/
	if(RightLine == COLOR_WHITE && MiddleLine == COLOR_BLACK && LeftLine == COLOR_WHITE){
		move(speed, speed, 0, 0);
	}

	if(LeftLine == COLOR_BLACK && MiddleLine == COLOR_WHITE){
		move(speed, -(speed), 50, 0);
	}

	if(RightLine == COLOR_BLACK && MiddleLine == COLOR_WHITE){
		move(-(speed), speed, 50, 0);
	}
	/*----------------------------------------------------------------------------------------------------------------*/

	if(RightLine == COLOR_BLACK && MiddleLine == COLOR_BLACK && LeftLine == COLOR_WHITE) {
		rotate(speed, RIGHT);
	}

	if(LeftLine == COLOR_BLACK && MiddleLine == COLOR_BLACK && RightLine == COLOR_WHITE) {
		rotate(speed, LEFT);
	}
	/*----------------------------------------------------------------------------------------------------------------*/

	if(RightLine == COLOR_GREEN) {
		move(speed, speed, 35, 0);
		wait10Msec(200);
		rotate(speed, RIGHT);
	}

	if(LeftLine == COLOR_GREEN) {
		move(speed, speed, 35, 0);
		wait10Msec(200);
		rotate(speed, LEFT);
	}
	/*----------------------------------------------------------------------------------------------------------------*/

	if(LeftLine == COLOR_BLACK && RightLine == COLOR_BLACK && MiddleLine == COLOR_BLACK){
		move(speed, speed, 0, 0);
	}

	if(LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && MiddleLine == COLOR_WHITE) {
		FindLine(speed);
	}

	if(LeftLine == COLOR_BLACK && MiddleLine == COLOR_WHITE && RightLine == COLOR_BLACK) {
		FindLine(speed);
	}
}
