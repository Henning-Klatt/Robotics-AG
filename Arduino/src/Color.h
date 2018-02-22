#ifndef COLOR_H_
#define COLOR_H_

void Writei2cregisters(byte numberbytes, byte command, byte mode);
void Readi2cRegisters(int numberbytes, byte command, byte mode);
void init_TCS34725(byte mode);
void get_TCS34725ID(byte mode);
void get_Colors(byte mode);

#endif
