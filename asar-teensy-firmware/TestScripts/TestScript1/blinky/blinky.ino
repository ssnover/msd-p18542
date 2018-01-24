//blinky.ino
const int led = 13;

void setup() 
{
  pinMode(led, OUTPUT);

}

void loop()
{
  blinky(2000);

}

void blinky(const int rate)
{
  digitalWrite(led, HIGH);
  delay(rate);
  digitalWrite(led, LOW);
  delay(rate);
}

