#include <Servo.h>
#include <Keypad.h>
#include <Vector.h>

#define LED1 12
#define LED2 11
#define NUM_KEYS 3
#define relay 10

char key;
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {2,3,4,5};
byte colPins[COLS] = {6,7,8,9};
char mycode[NUM_KEYS] = {'5','6','7'};
char but_press[NUM_KEYS] = {};
int k = 0, s = 0; // Счетчик нажатий, счетчик совпадений

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup() {
  pinMode (LED1, OUTPUT);
  pinMode (LED2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  key = keypad.getKey();
  if (key != NO_KEY){
    Serial.print(key);
    but_press[k] = key;
    k++;
    if (k == NUM_KEYS){
      for(int i = 0; i<3; i++){
        Serial.print(but_press[i]);
        Serial.print(mycode[i]);
        if(but_press[i] == mycode[i]){
          Serial.print('Совпадение '+ but_press[i]);
        s++;
        }
      }
      Serial.print(s+1);
      if (s == NUM_KEYS){
        digitalWrite(LED1, HIGH);
        delay(2000);
        digitalWrite(LED1, LOW);
        s == 0;
        k == 0;
        but_press[NUM_KEYS] = {};
      }
      else {
        digitalWrite(LED2, HIGH);
        delay(1000);
        digitalWrite(LED2, LOW);
        k == 0;
        s == 0;
        but_press[NUM_KEYS] = {};
      }
    }

  }
  if (key == '0'){
    digitalWrite(LED2, HIGH);
    delay(1000);
    digitalWrite(LED2, LOW);
    k == 0;
    s == 0;
    but_press[NUM_KEYS] = {};
  }
}
