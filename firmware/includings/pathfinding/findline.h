void FindLine(const int speed){
	nxtDisplayClearTextLine(1);
	nxtDisplayString(1, "FindLine");

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
		else if(step >= 62){
			move(-speed, speed, 0, 0);
		}
		RefreshColor();
	}
}