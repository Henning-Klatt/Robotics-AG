void rotate (const int speed, const int direction) {
	nxtDisplayClearTextLine(3);
	nxtDisplayString(3, "Rotate %d", direction);
	move(speed, speed, 80, 0);
	RefreshColor();
	if (direction == RIGHT) {
		for(int count = 0; LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && count < 25; count++) {
			move(-speed, speed, 0, 0);
			RefreshColor();
		}
	} else if (direction == LEFT) {
			for(int count = 0; LeftLine == COLOR_WHITE && RightLine == COLOR_WHITE && count < 25; count++){
			move(speed, -speed, 0, 0);
			RefreshColor();
		}
	}
	move(0, 0, 0, 0);
	nxtDisplayClearTextLine(3);
}