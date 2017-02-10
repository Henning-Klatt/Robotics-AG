#include "includings/move.h"


void FindLine(const int speed);
void FollowLine(const int speed);
void rotate (const int speed, const int direction);

void rotate (const int speed, const int direction) {
		nxtDisplayClearTextLine(3);
		nxtDisplayString(3, "Rotate %d", direction);
		move(speed, speed, 80, 0);
		RefreshColor();
		if (direction == RIGHT) {
			for(int count = 0; LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && count < 100; count++) {
				move(-speed, speed, 0, 0);
				RefreshColor();
			}
		} else if (direction == LEFT) {
				for(int count = 0; LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && count < 100; count++){
				move(speed, -speed, 0, 0);
				RefreshColor();
			}
		}
		nxtDisplayClearTextLine(3);
	}


void FindLine(const int speed){
	nxtDisplayClearTextLine(1);
	nxtDisplayString(1, "FindLine");
	while(true) {
		for(int step = 0; LeftLine != COLOR_BLACK && MiddleLine != COLOR_BLACK && RightLine != COLOR_BLACK && step < 20; step++) {
			nxtDisplayClearTextLine(3);
			nxtDisplayString(3, "Vor: %d", step);
			move(speed, speed, 0, 0);
			RefreshColor();
		}
		for(int step = 0; LeftLine != COLOR_BLACK && MiddleLine != COLOR_BLACK && RightLine != COLOR_BLACK && step < 80; step++) {
			nxtDisplayClearTextLine(3);
			nxtDisplayString(3, "Drehen: %d", step);
			if(step <= 20){
				move(-speed, speed, 0, 0);
			}
			else if(step < 40){
				move(speed, -speed, 0, 0);
			}
			else if(step >= 60){
				move(-speed, speed, 0, 0);
			}
			RefreshColor();
		}
		break;
	}
}


void FollowLine(const int speed){
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
		move(speed, speed, 25, 0);
		rotate(speed, RIGHT);
	}

	if(LeftLine == COLOR_GREEN) {
		move(speed, speed, 25, 0);
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
