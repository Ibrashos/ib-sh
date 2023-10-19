#include <Servo.h>
#include <Keypad.h>
#include <Vector.h>
#include <Servo.h>
#include <LiquidCrystal_I2C.h>

Servo myservo;

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

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  pinMode (LED1, OUTPUT);
  pinMode (LED2, OUTPUT);
  myservo.attach(13);
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
        if(but_press[i] == mycode[i]){
        s++;
        }
      }
      if (s == NUM_KEYS){
        lcd.setCursor(1,0);
        lcd.print("Opened!");
        myservo.write(0);
        digitalWrite(LED1, HIGH);
        delay(2000);
        digitalWrite(LED1, LOW);
        s = 0;
        k = 0;
        but_press[NUM_KEYS] = {};
        myservo.write(180);
        lcd.clear();
      }
      else {
        lcd.setCursor(1,0);
        lcd.print("Closed :( ");
        digitalWrite(LED2, HIGH);
        delay(1000);
        digitalWrite(LED2, LOW);
        k = 0;
        s = 0;
        but_press[NUM_KEYS] = {};
        lcd.clear();
      }
    }

  }
  if (key == '#') asm volatile("jmp 0x00");
  if (key == '0'){
    lcd.setCursor(1,0);
    lcd.print("Closed :( ");
    digitalWrite(LED2, HIGH);
    delay(1000);
    digitalWrite(LED2, LOW);
    k = 0;
    s = 0;
    but_press[NUM_KEYS] = {};
    lcd.clear();
  }
}
