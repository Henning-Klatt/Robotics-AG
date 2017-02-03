#include "includings/move.h"


void FindLine(const int speed);
void FollowLine(const int speed);
void rotate (const int speed, const int direction);

void rotate (const int speed, const int direction) {
		move(speed, speed, 80, 0);
		RefreshColor();

		if (direction == RIGHT) {
			for(int count = 0; LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && count < 100; count++) {
				move(-speed*2, speed*2, 1, 0.1);
				RefreshColor();
			}
		} else if (direction == LEFT) {
				for(int count = 0; LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && count < 100; count++){
				move(speed*2, -speed*2, 1, 0.1);
				RefreshColor();
			}
		}
	}


void FindLine(const int speed){
	while(true) {
		for(int step = 0; LeftLine != COLOR_BLACK && MiddleLine != COLOR_BLACK && RightLine != COLOR_BLACK && step < 50; step++) {
			move(speed, speed, 1, 0);
			RefreshColor();
		}
		for(int step = 0; LeftLine != COLOR_BLACK && MiddleLine != COLOR_BLACK && RightLine != COLOR_BLACK && step < 450; step++) {
			if(step <= 90){
				move(-speed, speed, 1, 0);
			}
			else if(step < 270){
				move(speed, -speed, 1,0);
			}
			else if(step >= 360){
				move(-speed, speed, 1, 0);
			}
		}
		break;
	}
}


void FollowLine(const int speed)
{
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
		move(speed, speed, 20, 0);
		rotate(speed, RIGHT);
	}

	if(LeftLine == COLOR_GREEN) {
		move(speed, speed, 20, 0);
		rotate(speed, LEFT);
	}
	/*----------------------------------------------------------------------------------------------------------------*/

	if(LeftLine == COLOR_BLACK && RightLine == COLOR_BLACK && MiddleLine == COLOR_BLACK){
		move(speed, speed, 1, 0);
	}

	if(LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && MiddleLine == COLOR_WHITE) {
		FindLine(speed);
	}

	if(LeftLine == COLOR_BLACK && MiddleLine == COLOR_WHITE && RightLine == COLOR_BLACK) {
		move(speed, speed, 1, 0);
	}
}
