/*
 * file: Proximity_Sensor.h
 * purpose: Low-Level Control proximity sensor (HCC-SR04)
 */
 
 #ifndef Proximity_Sensor_H
 #define Proximity_Sesnor_H
 
 namespace ASAR
 {
	 class Proximity_Sensor
	 {
		 public:
		
			Proximity_Sensor();
			~Proximity_Sensor();
			
			int CheckProximity();
			
			
		 
		 private:
		 
			const int trigPin = 21;  //Sensor Transmitter Pin
			const int echoPin = 20;  //Sensor Receiver Pin
  				  int duration = 0;  //Time taken to receive signal back (proportional to distance)
  				  double distance = 0; //Distance away from an object
			
		 
	 };
 }
 #endif
		 