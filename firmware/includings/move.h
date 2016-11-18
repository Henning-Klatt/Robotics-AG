#ifndef MOVE_H_
#define MOVE_H_

void move (const int Left, const int Right)
{
	motor[motorA] = Left;
	motor[motorB] = Right;
}

#endif
