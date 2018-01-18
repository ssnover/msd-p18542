/*
 * file: wheel-encoder.cpp
 * purpose: Implementation of the class for the magnetic wheel encoder.
 */

#include "Arduino.h"
#include "wheel-encoder.h"


namespace asar
{
namespace
{
// Encoder (Both Channels) Pulses / Shaft Revolution
constexpr uint32_t DEFAULT_CONVERSION_RATIO(48);
}

WHEEL_ENCODER::WHEEL_ENCODER(int channelAPin, int channelBPin, uint64_t ratioOutputToRPM)
    : my_channel_A_gpio(channelAPin),
      my_channel_B_gpio(channelBPin),
      my_ratio_of_encoder_channel_freq_to_shaft(ratioOutputToRPM)
{
    // Empty constructor
    attachInterrupt(digitalPinToInterrupt(this->my_channel_A_gpio),
                    this->incrementChannelACount, CHANGE);
    attachInterrupt(digitalPinToInterrupt(this->my_channel_B_gpio),
                    this->incrementChannelBCount, CHANGE);
}


WHEEL_ENCODER::~WHEEL_ENCODER()
{
    // Empty destructor
}


uint32_t WHEEL_ENCODER::getCount(CHANNEL channel)
{
    if (channel == CHANNEL::A)
    {
        return this->my_channel_A_count;
    }
    else
    {
        return this->my_channel_B_count;
    }
}


void WHEEL_ENCODER::incrementChannelACount(void)
{
    this->my_channel_A_count++;
}


void WHEEL_ENCODER::incrementChannelBCount(void)
{
    this->my_channel_B_count++;
}

} // namespace asar
