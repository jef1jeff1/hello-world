#!/bin/bash
# Convert all BMP animations to GIF

echo "Converting animations to GIF..."

# Bouncing ball
if [ -d "bounce_frames" ]; then
    convert bounce_frames/*.bmp -delay 8 -loop 0 bouncing_ball.gif
    echo "Created bouncing_ball.gif"
fi

# Spiral
if [ -d "spiral_frames" ]; then
    convert spiral_frames/*.bmp -delay 12 -loop 0 colorful_spiral.gif
    echo "Created colorful_spiral.gif"
fi

# Wave
if [ -d "wave_frames" ]; then
    convert wave_frames/*.bmp -delay 15 -loop 0 sine_wave.gif
    echo "Created sine_wave.gif"
fi

echo "All animations converted!"
echo "Generated GIF files:"
ls -la *.gif
