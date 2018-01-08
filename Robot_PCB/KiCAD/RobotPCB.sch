EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:MyLIB
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:RobotPCB-cache
EELAYER 25 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 1 1
Title "Robot PCB Schematic"
Date "2018-01-01"
Rev "3"
Comp "MSD P18542"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CON3_Servo J9
U 1 1 5A499C07
P 7200 4200
F 0 "J9" H 7500 4200 60  0000 C CNN
F 1 "CON3_Servo" H 7550 3550 60  0000 C CNN
F 2 "footprints:5-103634-2" H 7500 4200 60  0001 C CNN
F 3 "" H 7500 4200 60  0001 C CNN
F 4 "5-103634-2" H 7200 4200 60  0001 C CNN "P/N"
F 5 "TE Connectivity" H 7200 4200 60  0001 C CNN "MFG"
F 6 "CONN HEADER RTANG 3POS PCB TIN" H 7200 4200 60  0001 C CNN "Description"
F 7 "1.11" H 7200 4200 60  0001 C CNN "Cost"
	1    7200 4200
	1    0    0    -1  
$EndComp
$Comp
L CON14_TeensyRight J2
U 1 1 5A49A53F
P 3950 4900
F 0 "J2" H 3500 6450 60  0000 C CNN
F 1 "CON14_TeensyRight" H 3900 4800 60  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Straight_1x14_Pitch2.54mm" H 3900 4800 60  0001 C CNN
F 3 "" H 3900 4800 60  0001 C CNN
F 4 "PPTC141LFBN-RC" H 3950 4900 60  0001 C CNN "P/N"
F 5 "Sullins Connector" H 3950 4900 60  0001 C CNN "MFG"
F 6 "CONN HEADER FEMALE 14POS.1\" TIN" H 3950 4900 60  0001 C CNN "Description"
F 7 ".91" H 3950 4900 60  0001 C CNN "Cost"
	1    3950 4900
	1    0    0    -1  
$EndComp
$Comp
L CON14_TeensyLeft J1
U 1 1 5A49A720
P 2750 4950
F 0 "J1" H 3100 6550 60  0000 C CNN
F 1 "CON14_TeensyLeft" H 2800 4900 60  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Straight_1x14_Pitch2.54mm" H 3050 6600 60  0001 C CNN
F 3 "" H 3050 6600 60  0001 C CNN
F 4 "PPTC141LFBN-RC" H 2750 4950 60  0001 C CNN "P/N"
F 5 "Sullins Connector" H 2750 4950 60  0001 C CNN "MFG"
F 6 "CONN HEADER FEMALE 14POS.1\" TIN" H 2750 4950 60  0001 C CNN "Description"
F 7 "0.91" H 2750 4950 60  0001 C CNN "Cost"
	1    2750 4950
	1    0    0    -1  
$EndComp
$Comp
L CON5_XBEE J10
U 1 1 5A49A7FE
P 7200 6050
F 0 "J10" H 7550 6800 60  0000 C CNN
F 1 "CON5_XBEE" H 7550 6050 60  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Straight_1x05_Pitch2.54mm" H 7200 6050 60  0001 C CNN
F 3 "" H 7200 6050 60  0001 C CNN
F 4 "PPTC051LFBN-RC" H 7200 6050 60  0001 C CNN "P/N"
F 5 "Sullins Connector" H 7200 6050 60  0001 C CNN "MFG"
F 6 "CONN HEADER FEM 5POS .1\" SGL TIN" H 7200 6050 60  0001 C CNN "Description"
F 7 "0.47" H 7200 6050 60  0001 C CNN "Cost"
	1    7200 6050
	1    0    0    -1  
$EndComp
$Comp
L SW_SPST SW1
U 1 1 5A49AC00
P 2200 1650
F 0 "SW1" H 2200 1775 50  0000 C CNN
F 1 "SW_SPST" H 2200 1550 50  0000 C CNN
F 2 "footprints:WireConnection_1.20mmDrill" H 2200 1650 50  0001 C CNN
F 3 "" H 2200 1650 50  0001 C CNN
F 4 "100SP1T1B1M1QEH" H 2200 1650 60  0001 C CNN "P/N"
F 5 "E-Switch" H 2200 1650 60  0001 C CNN "MFG"
F 6 "SWITCH TOGGLE SPDT 5A 120V" H 2200 1650 60  0001 C CNN "Description"
F 7 "2.11" H 2200 1650 60  0001 C CNN "Cost"
	1    2200 1650
	1    0    0    -1  
$EndComp
$Comp
L L7805 U1
U 1 1 5A49AC4D
P 3700 1150
F 0 "U1" H 3550 1275 50  0000 C CNN
F 1 "L7805" H 3700 1275 50  0000 L CNN
F 2 "Power_Integrations:TO-220" H 3725 1000 50  0001 L CIN
F 3 "" H 3700 1100 50  0001 C CNN
F 4 "L7805CV" H 3700 1150 60  0001 C CNN "P/N"
F 5 "STMicroelectronics" H 3700 1150 60  0001 C CNN "MFG"
F 6 "IC REG LINEAR 5V 1.5A TO220AB" H 3700 1150 60  0001 C CNN "Description"
F 7 "0.45" H 3700 1150 60  0001 C CNN "Cost"
	1    3700 1150
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 5A49ADA0
P 3050 1400
F 0 "C1" H 3075 1500 50  0000 L CNN
F 1 ".33uF" H 3075 1300 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 3088 1250 50  0001 C CNN
F 3 "" H 3050 1400 50  0001 C CNN
F 4 "MURATA" H 3050 1400 60  0001 C CNN "MFG"
F 5 "CAP CER 0.33UF 50V X7R 1206" H 3050 1400 60  0001 C CNN "Description"
F 6 "GRM319R71H334KA01D" H 3050 1400 60  0001 C CNN "P/N"
F 7 ".44" H 3050 1400 60  0001 C CNN "Cost"
	1    3050 1400
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 5A49ADF9
P 4250 1400
F 0 "C2" H 4275 1500 50  0000 L CNN
F 1 ".1uF" H 4275 1300 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 4288 1250 50  0001 C CNN
F 3 "" H 4250 1400 50  0001 C CNN
F 4 "GRM319R71H104KA01D" H 4250 1400 60  0001 C CNN "P/N"
F 5 "Murata" H 4250 1400 60  0001 C CNN "MFG"
F 6 "CAP CER 0.1UF 50V X7R 1206" H 4250 1400 60  0001 C CNN "Decription"
F 7 "0.26" H 4250 1400 60  0001 C CNN "Cost"
	1    4250 1400
	1    0    0    -1  
$EndComp
$Comp
L L293D U2
U 1 1 5A49B11B
P 3700 7100
F 0 "U2" H 3600 8150 60  0000 C CNN
F 1 "L293D" H 3550 7050 60  0000 C CNN
F 2 "footprints:L293D" H 3700 7100 60  0001 C CNN
F 3 "" H 3700 7100 60  0001 C CNN
F 4 "L293D" H 3700 7100 60  0001 C CNN "P/N"
F 5 "ST Microelectronics" H 3700 7100 60  0001 C CNN "MFG"
F 6 "IC MOTOR DRIVER PAR 16-DIP" H 3700 7100 60  0001 C CNN "Description"
F 7 "3.91" H 3700 7100 60  0001 C CNN "Cost"
	1    3700 7100
	1    0    0    -1  
$EndComp
$Comp
L Fuse F1
U 1 1 5A49B61B
P 2650 6450
F 0 "F1" V 2730 6450 50  0000 C CNN
F 1 "16V_2A" V 2575 6450 50  0000 C CNN
F 2 "footprints:RHEF100" V 2580 6450 50  0001 C CNN
F 3 "" H 2650 6450 50  0001 C CNN
F 4 "RHEF200" V 2650 6450 60  0001 C CNN "P/N"
F 5 "Littlefuse Inc." V 2650 6450 60  0001 C CNN "MFG"
F 6 "PTC RESET FUSE 16V 2A RADIAL" V 2650 6450 60  0001 C CNN "Description"
F 7 ".60" V 2650 6450 60  0001 C CNN "Cost"
	1    2650 6450
	0    1    1    0   
$EndComp
$Comp
L Fuse F2
U 1 1 5A49B6AC
P 4600 6450
F 0 "F2" V 4680 6450 50  0000 C CNN
F 1 "16V_2A" V 4525 6450 50  0000 C CNN
F 2 "footprints:RHEF100" V 4530 6450 50  0001 C CNN
F 3 "" H 4600 6450 50  0001 C CNN
F 4 "RHEF200" V 4600 6450 60  0001 C CNN "P/N"
F 5 "Littlefuse Inc." V 4600 6450 60  0001 C CNN "MFG"
F 6 "PTC RESET FUSE 16V 2A RADIAL" V 4600 6450 60  0001 C CNN "Description"
F 7 ".60" V 4600 6450 60  0001 C CNN "Cost"
	1    4600 6450
	0    1    1    0   
$EndComp
$Comp
L CON2_DC-MOTOR J7
U 1 1 5A49B867
P 1600 6750
F 0 "J7" H 1700 7250 60  0000 C CNN
F 1 "CON2_DC-MOTOR" H 1750 6700 60  0000 C CNN
F 2 "footprints:5-103634-1" H 1750 6700 60  0001 C CNN
F 3 "" H 1750 6700 60  0001 C CNN
F 4 "5-103634-1" H 1600 6750 60  0001 C CNN "P/N"
F 5 "TE Connectivity" H 1600 6750 60  0001 C CNN "MFG"
F 6 "CONN HEADER RTANG 2POS PCB TIN" H 1600 6750 60  0001 C CNN "Description"
F 7 "0.73" H 1600 6750 60  0001 C CNN "Cost"
	1    1600 6750
	1    0    0    -1  
$EndComp
$Comp
L CON2_DC-MOTOR J8
U 1 1 5A49B8A6
P 5450 6750
F 0 "J8" H 5550 7250 60  0000 C CNN
F 1 "CON2_DC-MOTOR" H 5600 6700 60  0000 C CNN
F 2 "footprints:5-103634-1" H 5600 6700 60  0001 C CNN
F 3 "" H 5600 6700 60  0001 C CNN
F 4 "5-103634-1" H 5450 6750 60  0001 C CNN "P/N"
F 5 "TE Connectivity" H 5450 6750 60  0001 C CNN "MFG"
F 6 "CONN HEADER RTANG 2POS PCB TIN" H 5450 6750 60  0001 C CNN "Description"
F 7 "0.73" H 5450 6750 60  0001 C CNN "Cost"
	1    5450 6750
	-1   0    0    -1  
$EndComp
$Comp
L Speaker SP1
U 1 1 5A49BAEE
P 7450 3500
F 0 "SP1" H 7500 3725 50  0000 R CNN
F 1 "Speaker" H 7500 3650 50  0000 R CNN
F 2 "footprints:BUZZER" H 7450 3300 50  0001 C CNN
F 3 "" H 7440 3450 50  0001 C CNN
F 4 "PS1240P02BT" H 7450 3500 60  0001 C CNN "P/N"
F 5 "TDK" H 7450 3500 60  0001 C CNN "MFG"
F 6 "AUDIO PIEZO TRANSDUCER 30V TH" H 7450 3500 60  0001 C CNN "Description"
F 7 "0.72" H 7450 3500 60  0001 C CNN "Cost"
	1    7450 3500
	1    0    0    -1  
$EndComp
$Comp
L CON5_HC-SR04 J3
U 1 1 5A49BC10
P 9300 1900
F 0 "J3" H 8950 2500 60  0000 C CNN
F 1 "CON5_HC-SR04" H 8900 1800 60  0000 C CNN
F 2 "footprints:5-103634-4" H 8900 1800 60  0001 C CNN
F 3 "" H 8900 1800 60  0001 C CNN
F 4 "5-103634-4" H 9300 1900 60  0001 C CNN "P/N"
F 5 "TE Connectivity" H 9300 1900 60  0001 C CNN "MFG"
F 6 "CONN HEADER RTANG 5POS PCB TIN" H 9300 1900 60  0001 C CNN "Description"
F 7 "1.32" H 9300 1900 60  0001 C CNN "Cost"
	1    9300 1900
	-1   0    0    -1  
$EndComp
$Comp
L Con4_FlameSensor J4
U 1 1 5A49BF53
P 9350 3350
F 0 "J4" H 9050 4000 60  0000 C CNN
F 1 "Con4_FlameSensor" H 9000 3250 60  0000 C CNN
F 2 "footprints:5-103634-3" H 9000 3250 60  0001 C CNN
F 3 "" H 9000 3250 60  0001 C CNN
F 4 "5-103634-3" H 9350 3350 60  0001 C CNN "P/N"
F 5 "TE Connectivity" H 9350 3350 60  0001 C CNN "MFG"
F 6 "CONN HEADER RTANG 4POS PCB TIN" H 9350 3350 60  0001 C CNN "Description"
F 7 "1.30" H 9350 3350 60  0001 C CNN "Cost"
	1    9350 3350
	-1   0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 5A49C88A
P 5500 1750
F 0 "R2" V 5580 1750 50  0000 C CNN
F 1 "R_1K" V 5500 1750 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 5430 1750 50  0001 C CNN
F 3 "" H 5500 1750 50  0001 C CNN
F 4 "RC1206JR-071KL" V 5500 1750 60  0001 C CNN "P/N"
F 5 "Yageo" V 5500 1750 60  0001 C CNN "MFG"
F 6 "RES SMD 1K OHM 5% 1/4W 1206" V 5500 1750 60  0001 C CNN "Description"
F 7 "0.10" V 5500 1750 60  0001 C CNN "Cost"
	1    5500 1750
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 5A49C8FF
P 5950 1750
F 0 "R3" V 6030 1750 50  0000 C CNN
F 1 "R_150" V 5950 1750 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 5880 1750 50  0001 C CNN
F 3 "" H 5950 1750 50  0001 C CNN
F 4 "RC1206JR-07150RL" V 5950 1750 60  0001 C CNN "P/N"
F 5 "Yageo" V 5950 1750 60  0001 C CNN "MFG"
F 6 "RES SMD 150 OHM 5% 1/4W 1206" V 5950 1750 60  0001 C CNN "Description"
F 7 "0.10" V 5950 1750 60  0001 C CNN "Cost"
	1    5950 1750
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 5A49C954
P 6400 1750
F 0 "R4" V 6480 1750 50  0000 C CNN
F 1 "R_59" V 6400 1750 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 6330 1750 50  0001 C CNN
F 3 "" H 6400 1750 50  0001 C CNN
F 4 "RC1206FR-0759RL" V 6400 1750 60  0001 C CNN "P/N"
F 5 "Yageo" V 6400 1750 60  0001 C CNN "MFG"
F 6 "RES SMD 59 OHM 1% 1/4W 1206" V 6400 1750 60  0001 C CNN "Description"
F 7 "0.10" V 6400 1750 60  0001 C CNN "Cost"
	1    6400 1750
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 5A49C9C3
P 6800 1750
F 0 "R5" V 6880 1750 50  0000 C CNN
F 1 "R_59" V 6800 1750 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 6730 1750 50  0001 C CNN
F 3 "" H 6800 1750 50  0001 C CNN
F 4 "RC1206FR-0759RL" V 6800 1750 60  0001 C CNN "P/N"
F 5 "Yageo" V 6800 1750 60  0001 C CNN "MFG"
F 6 "RES SMD 59 OHM 1% 1/4W 1206" V 6800 1750 60  0001 C CNN "Description"
F 7 "0.10" V 6800 1750 60  0001 C CNN "Cost"
	1    6800 1750
	1    0    0    -1  
$EndComp
$Comp
L LED D3
U 1 1 5A49CB86
P 6400 2300
F 0 "D3" H 6400 2400 50  0000 C CNN
F 1 "LED_GRN" H 6400 2150 50  0000 C CNN
F 2 "LEDs:LED_D5.0mm" H 6400 2300 50  0001 C CNN
F 3 "" H 6400 2300 50  0001 C CNN
F 4 "LTL-4233" H 6400 2300 60  0001 C CNN "P/N"
F 5 "Lite-On Inc." H 6400 2300 60  0001 C CNN "MFG"
F 6 "LED GRN DIFF 5MM ROUND T/H" H 6400 2300 60  0001 C CNN "Description"
F 7 "0.36" H 6400 2300 60  0001 C CNN "Cost"
	1    6400 2300
	0    -1   -1   0   
$EndComp
$Comp
L LED D4
U 1 1 5A49CBDD
P 6800 2300
F 0 "D4" H 6800 2400 50  0000 C CNN
F 1 "LED_GRN" H 6800 2150 50  0000 C CNN
F 2 "LEDs:LED_D5.0mm" H 6800 2300 50  0001 C CNN
F 3 "" H 6800 2300 50  0001 C CNN
F 4 "LTL-4233" H 6800 2300 60  0001 C CNN "P/N"
F 5 "Lite-On Inc." H 6800 2300 60  0001 C CNN "MFG"
F 6 "LED GRN DIFF 5MM ROUND T/H" H 6800 2300 60  0001 C CNN "Description"
F 7 "0.36" H 6800 2300 60  0001 C CNN "Cost"
	1    6800 2300
	0    -1   -1   0   
$EndComp
$Comp
L LED D1
U 1 1 5A49CC40
P 5500 2300
F 0 "D1" H 5500 2400 50  0000 C CNN
F 1 "LED_GRN" H 5500 2150 50  0000 C CNN
F 2 "LEDs:LED_D5.0mm" H 5500 2300 50  0001 C CNN
F 3 "" H 5500 2300 50  0001 C CNN
F 4 "LTL-4233" H 5500 2300 60  0001 C CNN "P/N"
F 5 "Lite-On Inc." H 5500 2300 60  0001 C CNN "MFG"
F 6 "LED GRN DIFF 5MM ROUND T/H" H 5500 2300 60  0001 C CNN "Description"
F 7 "0.36" H 5500 2300 60  0001 C CNN "Cost"
	1    5500 2300
	0    -1   -1   0   
$EndComp
$Comp
L LED D2
U 1 1 5A49CC9B
P 5950 2300
F 0 "D2" H 5950 2400 50  0000 C CNN
F 1 "LED_GRN" H 5950 2150 50  0000 C CNN
F 2 "LEDs:LED_D5.0mm" H 5950 2300 50  0001 C CNN
F 3 "" H 5950 2300 50  0001 C CNN
F 4 "LTL-4233" H 5950 2300 60  0001 C CNN "P/N"
F 5 "Lite-On Inc." H 5950 2300 60  0001 C CNN "MFG"
F 6 "LED GRN DIFF 5MM ROUND T/H" H 5950 2300 60  0001 C CNN "Description"
F 7 "0.36" H 5950 2300 60  0001 C CNN "Cost"
	1    5950 2300
	0    -1   -1   0   
$EndComp
$Comp
L Earth #PWR01
U 1 1 5A4A266E
P 3350 1750
F 0 "#PWR01" H 3350 1500 50  0001 C CNN
F 1 "Earth" H 3350 1600 50  0001 C CNN
F 2 "" H 3350 1750 50  0001 C CNN
F 3 "" H 3350 1750 50  0001 C CNN
	1    3350 1750
	1    0    0    -1  
$EndComp
$Comp
L +BATT #PWR02
U 1 1 5A4A282C
P 2850 1050
F 0 "#PWR02" H 2850 900 50  0001 C CNN
F 1 "+BATT" H 2850 1190 50  0000 C CNN
F 2 "" H 2850 1050 50  0001 C CNN
F 3 "" H 2850 1050 50  0001 C CNN
	1    2850 1050
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR03
U 1 1 5A4A2A74
P 4250 1050
F 0 "#PWR03" H 4250 900 50  0001 C CNN
F 1 "+5V" H 4250 1190 50  0000 C CNN
F 2 "" H 4250 1050 50  0001 C CNN
F 3 "" H 4250 1050 50  0001 C CNN
	1    4250 1050
	1    0    0    -1  
$EndComp
$Comp
L +BATT #PWR04
U 1 1 5A4A3111
P 5500 1450
F 0 "#PWR04" H 5500 1300 50  0001 C CNN
F 1 "+BATT" H 5500 1590 50  0000 C CNN
F 2 "" H 5500 1450 50  0001 C CNN
F 3 "" H 5500 1450 50  0001 C CNN
	1    5500 1450
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR05
U 1 1 5A4A315B
P 5950 1450
F 0 "#PWR05" H 5950 1300 50  0001 C CNN
F 1 "+5V" H 5950 1590 50  0000 C CNN
F 2 "" H 5950 1450 50  0001 C CNN
F 3 "" H 5950 1450 50  0001 C CNN
	1    5950 1450
	1    0    0    -1  
$EndComp
$Comp
L +3V3 #PWR06
U 1 1 5A4A31A5
P 6400 1450
F 0 "#PWR06" H 6400 1300 50  0001 C CNN
F 1 "+3V3" H 6400 1590 50  0000 C CNN
F 2 "" H 6400 1450 50  0001 C CNN
F 3 "" H 6400 1450 50  0001 C CNN
	1    6400 1450
	1    0    0    -1  
$EndComp
$Comp
L Earth #PWR07
U 1 1 5A4A8A5D
P 2400 3400
F 0 "#PWR07" H 2400 3150 50  0001 C CNN
F 1 "Earth" H 2400 3250 50  0001 C CNN
F 2 "" H 2400 3400 50  0001 C CNN
F 3 "" H 2400 3400 50  0001 C CNN
	1    2400 3400
	1    0    0    -1  
$EndComp
Text Label 2150 3700 0    60   ~ 0
XBEE_Tx
Text Label 2150 3600 0    60   ~ 0
XBEE_Rx
Text Label 2150 3800 0    60   ~ 0
XBEE_RESET
Text Label 2150 3900 0    60   ~ 0
PWM_LeftA
Text Label 2150 4000 0    60   ~ 0
PWM_LeftB
Text Label 2150 4100 0    60   ~ 0
PWM_RightA
Text Label 2150 4200 0    60   ~ 0
PWM_RightB
Text Label 2150 4300 0    60   ~ 0
EnableLeft
Text Label 2150 4400 0    60   ~ 0
EnableRight
Text Label 2150 4500 0    60   ~ 0
ServoSignal
Text Label 2150 4600 0    60   ~ 0
PiezoSpeak
$Comp
L +5V #PWR08
U 1 1 5A4A9A59
P 4150 3400
F 0 "#PWR08" H 4150 3250 50  0001 C CNN
F 1 "+5V" H 4150 3540 50  0000 C CNN
F 2 "" H 4150 3400 50  0001 C CNN
F 3 "" H 4150 3400 50  0001 C CNN
	1    4150 3400
	1    0    0    -1  
$EndComp
$Comp
L Earth #PWR09
U 1 1 5A4A9AA3
P 4300 3550
F 0 "#PWR09" H 4300 3300 50  0001 C CNN
F 1 "Earth" H 4300 3400 50  0001 C CNN
F 2 "" H 4300 3550 50  0001 C CNN
F 3 "" H 4300 3550 50  0001 C CNN
	1    4300 3550
	1    0    0    -1  
$EndComp
$Comp
L +3V3 #PWR010
U 1 1 5A4A9AED
P 4450 3500
F 0 "#PWR010" H 4450 3350 50  0001 C CNN
F 1 "+3V3" H 4450 3640 50  0000 C CNN
F 2 "" H 4450 3500 50  0001 C CNN
F 3 "" H 4450 3500 50  0001 C CNN
	1    4450 3500
	1    0    0    -1  
$EndComp
Text Label 3950 4000 0    60   ~ 0
Encoder_OUTA1
Text Label 3950 4100 0    60   ~ 0
Encoder_OUTB1
Text Label 3950 4200 0    60   ~ 0
Encoder_OUTA2
Text Label 3950 4300 0    60   ~ 0
Encoder_OUTB2
Text Label 3950 4400 0    60   ~ 0
FlameDigital
Text Label 3950 4500 0    60   ~ 0
FlameAnalog
Text Label 3950 4600 0    60   ~ 0
PingTrig
Text Label 3950 4700 0    60   ~ 0
PingEcho
Text Label 3950 4800 0    60   ~ 0
Debug
Text Label 6800 1400 0    60   ~ 0
Debug
Wire Wire Line
	5500 1900 5500 2150
Wire Wire Line
	5950 1900 5950 2150
Wire Wire Line
	6400 1900 6400 2150
Wire Wire Line
	6800 1900 6800 2150
Wire Wire Line
	1500 1150 3400 1150
Wire Wire Line
	1700 1400 1500 1400
Wire Wire Line
	2400 1650 4250 1650
Wire Wire Line
	1700 1400 1700 1650
Wire Wire Line
	1700 1650 2000 1650
Wire Wire Line
	3050 1250 3050 1150
Connection ~ 3050 1150
Wire Wire Line
	3050 1650 3050 1550
Connection ~ 3050 1650
Wire Wire Line
	3700 1650 3700 1450
Connection ~ 3700 1650
Wire Wire Line
	4250 1650 4250 1550
Wire Wire Line
	4000 1150 4250 1150
Wire Wire Line
	4250 1050 4250 1250
Wire Wire Line
	3350 1650 3350 1750
Connection ~ 3350 1650
Wire Wire Line
	2850 1050 2850 1150
Connection ~ 2850 1150
Connection ~ 4250 1150
Wire Wire Line
	5500 1450 5500 1600
Wire Wire Line
	5950 1450 5950 1600
Wire Wire Line
	6400 1450 6400 1600
Wire Wire Line
	5500 2450 5500 2600
Wire Wire Line
	5500 2600 6800 2600
Wire Wire Line
	6800 2600 6800 2450
Wire Wire Line
	6400 2450 6400 2600
Connection ~ 6400 2600
Wire Wire Line
	5950 2450 5950 2600
Connection ~ 5950 2600
Wire Wire Line
	2750 3500 2650 3500
Wire Wire Line
	2650 3500 2650 3300
Wire Wire Line
	2650 3300 2400 3300
Wire Wire Line
	2400 3300 2400 3400
Wire Wire Line
	1600 3600 2750 3600
Wire Wire Line
	1600 3700 2750 3700
Wire Wire Line
	1600 3800 2750 3800
Wire Wire Line
	1600 3900 2750 3900
Wire Wire Line
	1600 4000 2750 4000
Wire Wire Line
	1600 4100 2750 4100
Wire Wire Line
	1600 4200 2750 4200
Wire Wire Line
	1600 4300 2750 4300
Wire Wire Line
	1600 4400 2750 4400
Wire Wire Line
	1600 4500 2750 4500
Wire Wire Line
	1600 4600 2750 4600
Wire Wire Line
	3950 3500 4150 3500
Wire Wire Line
	4150 3500 4150 3400
Wire Wire Line
	3950 3600 4200 3600
Wire Wire Line
	4200 3600 4200 3500
Wire Wire Line
	4200 3500 4300 3500
Wire Wire Line
	4300 3500 4300 3550
Wire Wire Line
	3950 3700 4450 3700
Wire Wire Line
	4450 3700 4450 3500
Wire Wire Line
	3950 4000 5450 4000
Wire Wire Line
	3950 4100 5450 4100
Wire Wire Line
	3950 4200 5450 4200
Wire Wire Line
	3950 4300 5450 4300
Wire Wire Line
	3950 4400 5450 4400
Wire Wire Line
	3950 4500 5450 4500
Wire Wire Line
	3950 4600 5450 4600
Wire Wire Line
	3950 4700 5450 4700
Wire Wire Line
	3950 4800 5450 4800
Wire Wire Line
	6800 1400 6800 1600
Wire Wire Line
	6800 1400 7150 1400
Wire Wire Line
	2500 6450 2050 6450
Wire Wire Line
	2050 6750 2050 6600
Text Label 2100 6450 0    60   ~ 0
MOT1+
Text Label 2100 6750 0    60   ~ 0
MOT1-
$Comp
L Earth #PWR011
U 1 1 5A4ABCE4
P 2900 6600
F 0 "#PWR011" H 2900 6350 50  0001 C CNN
F 1 "Earth" H 2900 6450 50  0001 C CNN
F 2 "" H 2900 6600 50  0001 C CNN
F 3 "" H 2900 6600 50  0001 C CNN
	1    2900 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2900 6550 3050 6550
Wire Wire Line
	2900 6550 2900 6600
Wire Wire Line
	2500 6850 3050 6850
Wire Wire Line
	3050 6250 2550 6250
Wire Wire Line
	3050 6350 2550 6350
Text Label 2550 6250 0    60   ~ 0
EnableLeft
Text Label 2550 6350 0    60   ~ 0
PWM_LeftA
Wire Wire Line
	3050 6450 2800 6450
Wire Wire Line
	2050 6750 3050 6750
Text Label 2500 6850 0    60   ~ 0
PWM_LeftB
$Comp
L +BATT #PWR012
U 1 1 5A4ACF4B
P 2650 7100
F 0 "#PWR012" H 2650 6950 50  0001 C CNN
F 1 "+BATT" H 2650 7240 50  0000 C CNN
F 2 "" H 2650 7100 50  0001 C CNN
F 3 "" H 2650 7100 50  0001 C CNN
	1    2650 7100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3050 6950 3050 7150
Wire Wire Line
	3050 7150 2650 7150
Wire Wire Line
	2650 7150 2650 7100
$Comp
L +5V #PWR013
U 1 1 5A4AD9D0
P 4350 6150
F 0 "#PWR013" H 4350 6000 50  0001 C CNN
F 1 "+5V" H 4350 6290 50  0000 C CNN
F 2 "" H 4350 6150 50  0001 C CNN
F 3 "" H 4350 6150 50  0001 C CNN
	1    4350 6150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 6250 4350 6250
Wire Wire Line
	4350 6250 4350 6150
Wire Wire Line
	4100 6350 4450 6350
Text Label 4100 6350 0    60   ~ 0
PWM_RightA
Wire Wire Line
	4100 6450 4450 6450
Wire Wire Line
	4750 6450 5000 6450
Wire Wire Line
	4100 6750 5000 6750
Wire Wire Line
	5000 6750 5000 6600
Text Label 4750 6450 0    60   ~ 0
MOT2+
Text Label 4650 6750 0    60   ~ 0
MOT2-
$Comp
L Earth #PWR014
U 1 1 5A4ADEBB
P 4400 6600
F 0 "#PWR014" H 4400 6350 50  0001 C CNN
F 1 "Earth" H 4400 6450 50  0001 C CNN
F 2 "" H 4400 6600 50  0001 C CNN
F 3 "" H 4400 6600 50  0001 C CNN
	1    4400 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 6650 4150 6650
Wire Wire Line
	4150 6650 4150 6550
Wire Wire Line
	4100 6550 4400 6550
Wire Wire Line
	4400 6550 4400 6600
Connection ~ 4150 6550
Wire Wire Line
	3050 6650 3000 6650
Wire Wire Line
	3000 6650 3000 6550
Connection ~ 3000 6550
Wire Wire Line
	4100 6850 4550 6850
Wire Wire Line
	4100 6950 4550 6950
Text Label 4100 6850 0    60   ~ 0
PWM_RightB
Text Label 4100 6950 0    60   ~ 0
EnableRight
Wire Wire Line
	6800 3500 7250 3500
Text Label 6800 3500 0    60   ~ 0
PiezoSpeak
$Comp
L Earth #PWR015
U 1 1 5A4AEBB1
P 6950 3650
F 0 "#PWR015" H 6950 3400 50  0001 C CNN
F 1 "Earth" H 6950 3500 50  0001 C CNN
F 2 "" H 6950 3650 50  0001 C CNN
F 3 "" H 6950 3650 50  0001 C CNN
	1    6950 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	7250 3600 6950 3600
Wire Wire Line
	6950 3600 6950 3650
Text Label 6750 4400 0    60   ~ 0
ServoSignal
Wire Wire Line
	7200 4400 6750 4400
$Comp
L +5V #PWR016
U 1 1 5A4AF19E
P 6600 4450
F 0 "#PWR016" H 6600 4300 50  0001 C CNN
F 1 "+5V" H 6600 4590 50  0000 C CNN
F 2 "" H 6600 4450 50  0001 C CNN
F 3 "" H 6600 4450 50  0001 C CNN
	1    6600 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 4550 6600 4550
Wire Wire Line
	6600 4550 6600 4450
$Comp
L Earth #PWR017
U 1 1 5A4AF2D5
P 6900 4750
F 0 "#PWR017" H 6900 4500 50  0001 C CNN
F 1 "Earth" H 6900 4600 50  0001 C CNN
F 2 "" H 6900 4750 50  0001 C CNN
F 3 "" H 6900 4750 50  0001 C CNN
	1    6900 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 4700 6900 4700
Wire Wire Line
	6900 4700 6900 4750
$Comp
L +5V #PWR018
U 1 1 5A4AF495
P 7000 5450
F 0 "#PWR018" H 7000 5300 50  0001 C CNN
F 1 "+5V" H 7000 5590 50  0000 C CNN
F 2 "" H 7000 5450 50  0001 C CNN
F 3 "" H 7000 5450 50  0001 C CNN
	1    7000 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 5500 7000 5500
Wire Wire Line
	7000 5500 7000 5450
$Comp
L Earth #PWR019
U 1 1 5A4AF59A
P 6800 5500
F 0 "#PWR019" H 6800 5250 50  0001 C CNN
F 1 "Earth" H 6800 5350 50  0001 C CNN
F 2 "" H 6800 5500 50  0001 C CNN
F 3 "" H 6800 5500 50  0001 C CNN
	1    6800 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 5600 6950 5600
Wire Wire Line
	6950 5600 6950 5450
Wire Wire Line
	6950 5450 6800 5450
Wire Wire Line
	6800 5450 6800 5500
Text Label 6850 5700 0    60   ~ 0
XBEE_Tx
Text Label 6850 5800 0    60   ~ 0
XBEE_Rx
Text Label 6700 5900 0    60   ~ 0
XBEE_RESET
Wire Wire Line
	7200 5700 6850 5700
Wire Wire Line
	7200 5800 6850 5800
Wire Wire Line
	7200 5900 6700 5900
$Comp
L +5V #PWR020
U 1 1 5A4AFC4E
P 9100 1400
F 0 "#PWR020" H 9100 1250 50  0001 C CNN
F 1 "+5V" H 9100 1540 50  0000 C CNN
F 2 "" H 9100 1400 50  0001 C CNN
F 3 "" H 9100 1400 50  0001 C CNN
	1    9100 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	9300 1450 9100 1450
Wire Wire Line
	9100 1450 9100 1400
Text Label 8950 1550 0    60   ~ 0
PingTrig
Text Label 8950 1650 0    60   ~ 0
PingEcho
Wire Wire Line
	9300 1550 8950 1550
Wire Wire Line
	9300 1650 8950 1650
$Comp
L Earth #PWR021
U 1 1 5A4AFF57
P 9050 1800
F 0 "#PWR021" H 9050 1550 50  0001 C CNN
F 1 "Earth" H 9050 1650 50  0001 C CNN
F 2 "" H 9050 1800 50  0001 C CNN
F 3 "" H 9050 1800 50  0001 C CNN
	1    9050 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	9300 1750 9050 1750
Wire Wire Line
	9050 1750 9050 1800
Text Label 8800 2900 0    60   ~ 0
FlameDigital
Text Label 8800 3200 0    60   ~ 0
FlameAnalog
Wire Wire Line
	9350 2900 8800 2900
Wire Wire Line
	9350 3200 8800 3200
$Comp
L Earth #PWR022
U 1 1 5A4B0545
P 8650 3150
F 0 "#PWR022" H 8650 2900 50  0001 C CNN
F 1 "Earth" H 8650 3000 50  0001 C CNN
F 2 "" H 8650 3150 50  0001 C CNN
F 3 "" H 8650 3150 50  0001 C CNN
	1    8650 3150
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR023
U 1 1 5A4B058F
P 8650 2900
F 0 "#PWR023" H 8650 2750 50  0001 C CNN
F 1 "+5V" H 8650 3040 50  0000 C CNN
F 2 "" H 8650 2900 50  0001 C CNN
F 3 "" H 8650 2900 50  0001 C CNN
	1    8650 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9350 3000 8650 3000
Wire Wire Line
	8650 3000 8650 2900
Wire Wire Line
	9350 3100 8650 3100
Wire Wire Line
	8650 3100 8650 3150
$Comp
L CON6_M-Encoder J5
U 1 1 5A4B0B23
P 9250 4700
F 0 "J5" H 8850 5500 60  0000 C CNN
F 1 "CON6_M-Encoder" H 8900 4600 60  0000 C CNN
F 2 "footprints:5-103634-5" H 8900 4600 60  0001 C CNN
F 3 "" H 8900 4600 60  0001 C CNN
F 4 "5-103634-5" H 9250 4700 60  0001 C CNN "P/N"
F 5 "TE Connectivity" H 9250 4700 60  0001 C CNN "MFG"
F 6 "CONN HEADER RTANG 6POS PCB TIN" H 9250 4700 60  0001 C CNN "Description"
F 7 "1.40" H 9250 4700 60  0001 C CNN "Cost"
	1    9250 4700
	-1   0    0    -1  
$EndComp
$Comp
L CON6_M-Encoder J6
U 1 1 5A4B0BAE
P 9250 6000
F 0 "J6" H 8850 6800 60  0000 C CNN
F 1 "CON6_M-Encoder" H 8900 5900 60  0000 C CNN
F 2 "footprints:5-103634-5" H 8900 5900 60  0001 C CNN
F 3 "" H 8900 5900 60  0001 C CNN
F 4 "5-103634-5" H 9250 6000 60  0001 C CNN "P/N"
F 5 "TE Connectivity" H 9250 6000 60  0001 C CNN "MFG"
F 6 "CONN HEADER RTANG 6POS PCB TIN" H 9250 6000 60  0001 C CNN "Description"
F 7 "1.40" H 9250 6000 60  0001 C CNN "Cost"
	1    9250 6000
	-1   0    0    -1  
$EndComp
Text Label 8950 4100 0    60   ~ 0
MOT1+
Text Label 8950 4200 0    60   ~ 0
MOT1-
Text Label 8600 4500 0    60   ~ 0
Encoder_OUTA1
Text Label 8600 4600 0    60   ~ 0
Encoder_OUTB1
Wire Wire Line
	9250 4100 8950 4100
Wire Wire Line
	9250 4200 8950 4200
Wire Wire Line
	9250 4500 8600 4500
Wire Wire Line
	9250 4600 8600 4600
$Comp
L Earth #PWR024
U 1 1 5A4B139B
P 8750 4250
F 0 "#PWR024" H 8750 4000 50  0001 C CNN
F 1 "Earth" H 8750 4100 50  0001 C CNN
F 2 "" H 8750 4250 50  0001 C CNN
F 3 "" H 8750 4250 50  0001 C CNN
	1    8750 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	9250 4300 8850 4300
Wire Wire Line
	8850 4300 8850 4200
Wire Wire Line
	8850 4200 8750 4200
Wire Wire Line
	8750 4200 8750 4250
$Comp
L +5V #PWR025
U 1 1 5A4B1485
P 8550 4300
F 0 "#PWR025" H 8550 4150 50  0001 C CNN
F 1 "+5V" H 8550 4440 50  0000 C CNN
F 2 "" H 8550 4300 50  0001 C CNN
F 3 "" H 8550 4300 50  0001 C CNN
	1    8550 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	9250 4400 8550 4400
Wire Wire Line
	8550 4400 8550 4300
Text Label 8950 5400 0    60   ~ 0
MOT2+
Text Label 8950 5500 0    60   ~ 0
MOT2-
Text Label 8600 5800 0    60   ~ 0
Encoder_OUTA2
Text Label 8600 5900 0    60   ~ 0
Encoder_OUTB2
Wire Wire Line
	9250 5400 8950 5400
Wire Wire Line
	9250 5500 8950 5500
Wire Wire Line
	9250 5800 8600 5800
Wire Wire Line
	9250 5900 8600 5900
$Comp
L +5V #PWR026
U 1 1 5A4B1B64
P 8550 5600
F 0 "#PWR026" H 8550 5450 50  0001 C CNN
F 1 "+5V" H 8550 5740 50  0000 C CNN
F 2 "" H 8550 5600 50  0001 C CNN
F 3 "" H 8550 5600 50  0001 C CNN
	1    8550 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	9250 5600 8850 5600
$Comp
L Earth #PWR027
U 1 1 5A4B1FAD
P 8700 5550
F 0 "#PWR027" H 8700 5300 50  0001 C CNN
F 1 "Earth" H 8700 5400 50  0001 C CNN
F 2 "" H 8700 5550 50  0001 C CNN
F 3 "" H 8700 5550 50  0001 C CNN
	1    8700 5550
	1    0    0    -1  
$EndComp
Wire Wire Line
	8850 5600 8850 5500
Wire Wire Line
	8850 5500 8700 5500
Wire Wire Line
	8700 5500 8700 5550
Wire Wire Line
	9250 5700 8550 5700
Wire Wire Line
	8550 5700 8550 5600
$Comp
L TestHeaders J12
U 1 1 5A4B36BB
P 1600 4950
F 0 "J12" H 1600 6500 60  0000 C CNN
F 1 "TestHeaders" H 1550 4900 60  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x15_Pitch2.54mm" H 1600 4950 60  0001 C CNN
F 3 "" H 1600 4950 60  0001 C CNN
F 4 "PRPC015SAAN-RC" H 1600 4950 60  0001 C CNN "P/N"
F 5 "Sullins Connector" H 1600 4950 60  0001 C CNN "MFG"
F 6 "CONN HEADER .100\" SNGL STR 15POS" H 1600 4950 60  0001 C CNN "Description"
F 7 "0.38" H 1600 4950 60  0001 C CNN "Cost"
	1    1600 4950
	1    0    0    -1  
$EndComp
$Comp
L TestHeaders J13
U 1 1 5A4B3786
P 5450 4950
F 0 "J13" H 5450 6500 60  0000 C CNN
F 1 "TestHeaders" H 5400 4900 60  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x15_Pitch2.54mm" H 5450 4950 60  0001 C CNN
F 3 "" H 5450 4950 60  0001 C CNN
F 4 "PRPC015SAAN-RC" H 5450 4950 60  0001 C CNN "P/N"
F 5 "Sullins Connector" H 5450 4950 60  0001 C CNN "MFG"
F 6 "CONN HEADER .100\" SNGL STR 15POS" H 5450 4950 60  0001 C CNN "Description"
F 7 ".38" H 5450 4950 60  0001 C CNN "Cost"
	1    5450 4950
	-1   0    0    -1  
$EndComp
$Comp
L +BATT #PWR028
U 1 1 5A4B3B31
P 1850 3350
F 0 "#PWR028" H 1850 3200 50  0001 C CNN
F 1 "+BATT" H 1850 3490 50  0000 C CNN
F 2 "" H 1850 3350 50  0001 C CNN
F 3 "" H 1850 3350 50  0001 C CNN
	1    1850 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1850 3350 1850 3500
Wire Wire Line
	1850 3500 1600 3500
$Comp
L Earth #PWR029
U 1 1 5A4B47A4
P 2050 5000
F 0 "#PWR029" H 2050 4750 50  0001 C CNN
F 1 "Earth" H 2050 4850 50  0001 C CNN
F 2 "" H 2050 5000 50  0001 C CNN
F 3 "" H 2050 5000 50  0001 C CNN
	1    2050 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 4800 2050 5000
Wire Wire Line
	1600 4800 2050 4800
Wire Wire Line
	1600 4900 2050 4900
Connection ~ 2050 4900
$Comp
L +5V #PWR030
U 1 1 5A4B4AF8
P 5250 3400
F 0 "#PWR030" H 5250 3250 50  0001 C CNN
F 1 "+5V" H 5250 3540 50  0000 C CNN
F 2 "" H 5250 3400 50  0001 C CNN
F 3 "" H 5250 3400 50  0001 C CNN
	1    5250 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 3600 5450 3600
Wire Wire Line
	5250 3400 5250 3600
Wire Wire Line
	5450 3500 5250 3500
Wire Wire Line
	5250 3500 5250 3550
Connection ~ 5250 3550
$Comp
L +3V3 #PWR031
U 1 1 5A4B4D2D
P 4900 3650
F 0 "#PWR031" H 4900 3500 50  0001 C CNN
F 1 "+3V3" H 4900 3790 50  0000 C CNN
F 2 "" H 4900 3650 50  0001 C CNN
F 3 "" H 4900 3650 50  0001 C CNN
	1    4900 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 3700 4900 3700
Wire Wire Line
	4900 3650 4900 3800
Wire Wire Line
	4900 3800 5450 3800
Connection ~ 4900 3700
$Comp
L Earth #PWR032
U 1 1 5A4B571D
P 5150 5000
F 0 "#PWR032" H 5150 4750 50  0001 C CNN
F 1 "Earth" H 5150 4850 50  0001 C CNN
F 2 "" H 5150 5000 50  0001 C CNN
F 3 "" H 5150 5000 50  0001 C CNN
	1    5150 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 4900 5150 4900
Wire Wire Line
	5150 4900 5150 5000
Wire Wire Line
	3950 3900 5450 3900
Wire Wire Line
	1600 4700 2750 4700
$Comp
L Earth #PWR033
U 1 1 5A4A7344
P 6200 2750
F 0 "#PWR033" H 6200 2500 50  0001 C CNN
F 1 "Earth" H 6200 2600 50  0001 C CNN
F 2 "" H 6200 2750 50  0001 C CNN
F 3 "" H 6200 2750 50  0001 C CNN
	1    6200 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6200 2750 6200 2600
Connection ~ 6200 2600
NoConn ~ 3950 3800
NoConn ~ 2750 4800
NoConn ~ 9300 1850
$Comp
L R R1
U 1 1 5A4ACE43
P 5300 1750
F 0 "R1" V 5380 1750 50  0000 C CNN
F 1 "R_1K" V 5300 1750 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 5230 1750 50  0001 C CNN
F 3 "" H 5300 1750 50  0001 C CNN
F 4 "RC1206JR-071KL" V 5300 1750 60  0001 C CNN "P/N"
F 5 "Yageo" V 5300 1750 60  0001 C CNN "MFG"
F 6 "RES SMD 1K OHM 5% 1/4W 1206" V 5300 1750 60  0001 C CNN "Descrpition"
F 7 "0.10" V 5300 1750 60  0001 C CNN "Cost"
	1    5300 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 1600 5300 1550
Wire Wire Line
	5300 1550 5500 1550
Connection ~ 5500 1550
Wire Wire Line
	5300 1900 5300 2000
Wire Wire Line
	5300 2000 5500 2000
Connection ~ 5500 2000
$Comp
L CON2_Battery J11
U 1 1 5A49A9D5
P 1300 1600
F 0 "J11" H 1500 2300 60  0000 C CNN
F 1 "CON2_Battery" H 1500 1550 60  0000 C CNN
F 2 "Wire_Connections_Bridges:WireConnection_2.50mmDrill" H 1500 1550 60  0001 C CNN
F 3 "" H 1500 1550 60  0001 C CNN
	1    1300 1600
	-1   0    0    -1  
$EndComp
$Comp
L MountingHole MH1
U 1 1 5A523D83
P 700 3350
F 0 "MH1" H 700 3150 60  0000 C CNN
F 1 "MountingHole_4mm" H 900 3550 60  0000 C CNN
F 2 "Mounting_Holes:MountingHole_4mm_Pad" H 700 3350 60  0001 C CNN
F 3 "" H 700 3350 60  0001 C CNN
	1    700  3350
	1    0    0    -1  
$EndComp
$Comp
L MountingHole MH2
U 1 1 5A52415D
P 700 3850
F 0 "MH2" H 700 3650 60  0000 C CNN
F 1 "MountingHole_4mm" H 900 4050 60  0000 C CNN
F 2 "Mounting_Holes:MountingHole_4mm_Pad" H 700 3850 60  0001 C CNN
F 3 "" H 700 3850 60  0001 C CNN
	1    700  3850
	1    0    0    -1  
$EndComp
$Comp
L MountingHole MH3
U 1 1 5A5241D7
P 700 4350
F 0 "MH3" H 700 4150 60  0000 C CNN
F 1 "MountingHole_4mm" H 900 4550 60  0000 C CNN
F 2 "Mounting_Holes:MountingHole_4mm_Pad" H 700 4350 60  0001 C CNN
F 3 "" H 700 4350 60  0001 C CNN
	1    700  4350
	1    0    0    -1  
$EndComp
$Comp
L MountingHole MH4
U 1 1 5A52425C
P 700 4850
F 0 "MH4" H 700 4650 60  0000 C CNN
F 1 "MountingHole_4mm" H 900 5050 60  0000 C CNN
F 2 "Mounting_Holes:MountingHole_4mm_Pad" H 700 4850 60  0001 C CNN
F 3 "" H 700 4850 60  0001 C CNN
	1    700  4850
	1    0    0    -1  
$EndComp
$Comp
L GNDPWR #Chassis034
U 1 1 5A52443B
P 1050 5200
F 0 "#Chassis034" H 1050 5000 50  0001 C CNN
F 1 "GNDPWR" H 1050 5070 50  0001 C CNN
F 2 "" H 1050 5150 50  0001 C CNN
F 3 "" H 1050 5150 50  0001 C CNN
	1    1050 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	900  3350 1050 3350
Wire Wire Line
	1050 3350 1050 5200
Wire Wire Line
	900  3850 1050 3850
Connection ~ 1050 3850
Wire Wire Line
	900  4350 1050 4350
Connection ~ 1050 4350
Wire Wire Line
	900  4850 1050 4850
Connection ~ 1050 4850
$EndSCHEMATC
