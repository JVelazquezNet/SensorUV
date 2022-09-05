//Includes for LCD
#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;
int PIN_UV = A0; //Output to sensor
int PIN_REF33 = A1; //3.3V power on the Arduino board

int lectura;
int led1 = 9;  //Green Led
int led2 = 10; //Yellow Led 
int led3 = 11; //Orange Led
int led4 = 12; //Red Led

void setup() {
    //set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
         
    lcd.print("UV sensor");
    delay(1000);
    lcd.clear();
    
    Serial.begin(9600);

    pinMode(PIN_UV, INPUT);
    pinMode(PIN_REF33, INPUT);

    pinMode(led1, OUTPUT); //Define output pins to leds
    pinMode(led2, OUTPUT); //
    pinMode(led3, OUTPUT); //
    pinMode(led4, OUTPUT); //
     
    digitalWrite(led1, HIGH);  //Turn on leds for verification
    digitalWrite(led2, HIGH);  //
    digitalWrite(led3, HIGH);  // 
    digitalWrite(led4, HIGH);  // 
    delay(500);
}

void setOn(int status1, int status2, int status3, int status4)
{

  //flash leds according to the parameters 
  //given according to the intensity
  digitalWrite(led1, status1);  // 
  digitalWrite(led2, status2);  //
  digitalWrite(led3, status3);  //
  digitalWrite(led4, status4);  //
  delay(500);
  digitalWrite(led1, LOW);  //
  digitalWrite(led2, LOW);  //
  digitalWrite(led3, LOW);  //
  digitalWrite(led4, LOW);  //
  delay(100);
 
}

void loop() 
{
  int uvLevel = averageAnalogRead(PIN_UV);
  int refLevel = averageAnalogRead(PIN_REF33);
  //int index;
  int manualIndex;
  int mapIndex;
  
  lectura = analogRead(PIN_UV);
  //float voltaje = lectura*(3.3/669.0);

  //Use the 3.3V power pin as a reference to get a very accurate output value from sensor
  float outputVoltage = 3.3 / refLevel * uvLevel;
  
  float uvIntensity = mapfloat(outputVoltage, 0.99, 2.8, 0.0, 15.0); //Convert the voltage to a UV intensity level
 
  
  //Serial.print("output: ");
  //Serial.print(refLevel);
 
  //Serial.print(" ML8511 output: ");
  //Serial.print(uvLevel);

  //Serial.print(" Index: ");
  //Serial.print(map(uvLevel,0,refLevel,0,1023));
  //index = map(uvLevel,0,refLevel,0,1023);
  //indice = map(index,0,1023,0,10);
  
  //Serial.print(" "+String(indice));
  mapIndex = map(uvLevel,0,1023,0,10);
  //Serial.print(" "+String(indice));

   
  //Serial.print(" / ML8511 voltage: ");
  //Serial.print(outputVoltage);
 
  //Serial.print(" / UV Intensity (mW/cm^2): ");
  //Serial.print(uvIntensity); 
  
  int waveLength = map(uvLevel,0,refLevel,0,1023);  //with multiple readings

  //int waveLength = map(lectura,0,669,0,1023);         //with a single read
  
  if(waveLength < 50){
    manualIndex = 0;
  }
  else if(waveLength < 227){
    manualIndex = 1;
    setOn(1, 0, 0, 0 ); 
    delay(100); //retraso en milisegundos  
  }
  else if(waveLength < 318){
    manualIndex = 2;
    // verde
    setOn(1, 0, 0, 0 );
  }
  else if(waveLength < 408){
    manualIndex = 3;
   // amarillo
    setOn(0, 1, 0, 0 );
  }
  else if(waveLength < 503){
    manualIndex = 4;
   // amarillo
    setOn(0, 1, 0, 0 );
  }
  else if(waveLength < 606){
    manualIndex = 5;
    // amarillo
    setOn(0, 1, 0, 0 );
  }
  else if(waveLength < 696){
    manualIndex = 6;
    // naranja
    setOn(0, 0, 1, 0 );
  }
  else if(waveLength < 795){
    manualIndex = 7;
    // naranja
    setOn(0, 0, 1, 0 );
  }
  else if(waveLength < 881){
    manualIndex = 8;
    // rojo
    setOn(0, 0, 0, 1 );
  }
  else if(waveLength < 976){
    manualIndex = 9;
    // rojo
    setOn(0, 0, 0, 1 );
  }
  else{
    manualIndex = 10;
    // rojo
    setOn(0, 0, 0, 1 );
  }

  
  //Display the values ​​obtained on the LCD
  //lcd.autoscroll();
  lcd.setCursor(0, 0);
  //lcd.print("UV"+String(mapIndex) + " UV_INT " + String(uvIntensity) + " mW/cm^2");
  lcd.print(String(manualIndex) + "->" + String(mapIndex) + "->" + String(uvIntensity,4));
  lcd.setCursor(0, 1);
  lcd.print("R: "+String(waveLength)+ "<->"+String(outputVoltage)+"V");
  
  //lcd.clear();
  //lcd.setCursor(0, 0);
  Serial.println(String(manualIndex) + " " + String(uvIntensity,4));
  //lcd.setCursor(0, 1);
  //Serial.println(String(mapIndex) + " " + String(uvIntensity,4));
  
  
  delay(1000);
}

//Takes an average of readings on a given pin
//Returns the average
int averageAnalogRead(int pinToRead)
{
  byte numberOfReadings = 8;
  unsigned int runningValue = 0; 
 
  for(int x = 0 ; x < numberOfReadings ; x++)
    runningValue += analogRead(pinToRead);
  runningValue /= numberOfReadings;
 
  return(runningValue);
}

float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
