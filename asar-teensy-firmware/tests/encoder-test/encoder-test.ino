/*
 * file: encoder-test.ino
 * purpose: Test that the encoders are properly recording the rotation of the
 *          motor and the direction it's spinning.
 *
 *          Takes at least 20 seconds to run. Can run on prototype circuit or
 *          on PCB.
 */

#include "Arduino.h"
#include "wheel-encoder.h"


namespace
{
const int ENCODER_OUTA1(21);
const int ENCODER_OUTB1(20);
const int ENCODER_OUTA2(19);
const int ENCODER_OUTB2(18);
const int POLOLU_ENCODER_SIGNAL_RATIO(48);
ASAR::WHEEL_ENCODER left_encoder(ENCODER_OUTA1, ENCODER_OUTB1, POLOLU_ENCODER_SIGNAL_RATIO);
ASAR::WHEEL_ENCODER right_encoder(ENCODER_OUTA2, ENCODER_OUTB2, POLOLU_ENCODER_SIGNAL_RATIO);
} // namespace


void setup(void)
{
    Serial.begin(115200);
    // TODO: start turning the motors

    int count(0);

    while (true)
    {
        Serial.print("Left Encoder Count: ");
        Serial.println(left_encoder.getCount());
        Serial.print("Left Encoder Rotation Direction: ");
        Serial.println(left_encoder.getDirection());

        Serial.print("Right Encoder Count: ");
        Serial.println(right_encoder.getCount());
        Serial.print("Right Encoder Rotation Direction: ");
        Serial.println(right_encoder.getDirection());

        delay(1000);

        if (20 <= count)
        {
            // TODO: change direction of both motors
        }
    }
}


void loop(void)
{
}
