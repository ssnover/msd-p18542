const int trigPin = 2;
const int echoPin = 4;

void setup() {
  // initialize serial communication at a 9600 baud rate
  Serial.begin(9600);
}

void loop()
{
  // establish variables for duration of the ping and the distance result in centimeters:
  long duration, cm;

  //send trigger receive echo
  pinMode(trigPin, OUTPUT);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  //Take echo time as input
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);

  // convert the time into a distance
  cm = microsecondsToCentimeters(duration);
  //print reading
  Serial.print(cm);
  Serial.print("cm \n");
  if (cm <= 10) {  
  Serial.print("DANGER \n\n");
  }
  
  else if (cm > 100) {
  Serial.print("Nothing out here for miles \n\n");
  }
  delay(3000);
  
}

long microsecondsToCentimeters(long microseconds)
{
//Time to distance convertion
  return microseconds / 29 / 2;
}
