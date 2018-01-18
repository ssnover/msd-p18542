/*
 * file: wheel-encoder.h
 * purpose: Interface for magnetic wheel encoder.
 */


#ifndef WHEEL_ENCODER_H
#define WHEEL_ENCODER_H


#include <stdint.h>


namespace ASAR
{
class WHEEL_ENCODER
{
public:
    enum class ROTATIONAL_DIRECTION
    {
        DEFAULT             = 0u,
        CLOCKWISE           = 1u,
        COUNTERCLOCKWISE    = 2u,
    };

    enum class CHANNEL
    {
        A = 0u,
        B = 1u,
    };

    WHEEL_ENCODER(int channelAPin, int channelBPin, uint32_t ratioOutputToRPM);
    ~WHEEL_ENCODER();

    uint32_t getCount(CHANNEL channel);

    ROTATIONAL_DIRECTION getDirection();

private:
    int my_channel_A_gpio;
    int my_channel_B_gpio;
    uint32_t my_ratio_of_encoder_channel_freq_to_shaft;
    uint64_t my_channel_A_count = 0;
    uint64_t my_channel_B_count = 0;
    ROTATIONAL_DIRECTION my_direction_of_travel;

    void incrementChannelACount();
    void incrementChannelBCount();
};

} // namespace ASAR

#endif // WHEEL_ENCODER_H
