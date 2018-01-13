#include <Adafruit_MCP3008.h>

Adafruit_MCP3008 adc;

int count = 0;

void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  while (!Serial);

  Serial.println("MCP3008 simple test.");
  // (sck, mosi, miso, cs);
  adc.begin(10, 12, 11, 13);
  digitalWrite(5, HIGH);
  delay(50);
  digitalWrite(5, LOW);
  delay(200);
  digitalWrite(5, HIGH);
  delay(50);
  digitalWrite(5, LOW);
}

void loop() {
  /*for (int chan=0; chan<8; chan++) {
    Serial.print(adc.readADC(chan)); Serial.print("\t");
  }

  Serial.print("["); Serial.print(count); Serial.println("]");
  count++;
  
  delay(100);*/
  int button = analogRead(A0);
  if(button >= 900 && button <= 931 ){
    digitalWrite(5, HIGH);
  }
  else{
    digitalWrite(5, LOW);
  }
  delay(50);
  
}
