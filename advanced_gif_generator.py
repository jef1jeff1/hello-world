#!/usr/bin/env python3
"""
Advanced GIF Animation Generator
Creates multiple types of animated GIFs using only built-in Python libraries
"""

import os
import math
import struct

def create_bmp_frame(width, height, frame_data):
    """Create a BMP format frame"""
    # BMP header
    file_size = 54 + width * height * 3
    bmp_header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)
    
    # DIB header
    dib_header = struct.pack('<IIIHHIIIIII', 40, width, height, 1, 24, 0, 
                            width * height * 3, 2835, 2835, 0, 0)
    
    # Convert RGB to BGR and pad rows to 4-byte boundary
    bmp_data = bytearray()
    row_padding = (4 - (width * 3) % 4) % 4
    
    for y in range(height - 1, -1, -1):  # BMP stores bottom-to-top
        for x in range(width):
            idx = (y * width + x) * 3
            # Convert RGB to BGR
            bmp_data.extend([frame_data[idx + 2], frame_data[idx + 1], frame_data[idx]])
        # Add padding
        bmp_data.extend([0] * row_padding)
    
    return bmp_header + dib_header + bytes(bmp_data)

def create_bouncing_ball_animation():
    """Create a bouncing ball animation"""
    width, height = 200, 150
    frames = []
    num_frames = 30
    
    for frame_num in range(num_frames):
        frame_data = []
        
        # Calculate ball position (bouncing motion)
        t = frame_num / (num_frames - 1)
        ball_y = int(height * 0.8 * abs(math.sin(t * math.pi * 2)))
        ball_x = int(width * 0.1 + (width * 0.8) * t)
        ball_radius = 15
        
        # Create gradient background
        for y in range(height):
            for x in range(width):
                # Distance from ball center
                dist = math.sqrt((x - ball_x) ** 2 + (y - ball_y) ** 2)
                
                if dist <= ball_radius:
                    # Ball with gradient
                    intensity = max(0, 1 - (dist / ball_radius) * 0.7)
                    red = int(255 * intensity)
                    green = int(100 * intensity)
                    blue = int(50 * intensity)
                else:
                    # Background gradient
                    bg_intensity = 1 - (y / height) * 0.5
                    red = int(50 * bg_intensity)
                    green = int(100 * bg_intensity)
                    blue = int(200 * bg_intensity)
                
                frame_data.extend([red, green, blue])
        
        # Save as BMP
        bmp_data = create_bmp_frame(width, height, frame_data)
        frames.append((f"bounce_{frame_num:02d}.bmp", bmp_data))
    
    return frames

def create_spiral_animation():
    """Create a colorful spiral animation"""
    width, height = 200, 200
    frames = []
    num_frames = 24
    
    for frame_num in range(num_frames):
        frame_data = []
        
        # Rotation angle
        rotation = (frame_num / num_frames) * 2 * math.pi
        
        for y in range(height):
            for x in range(width):
                # Center coordinates
                cx = x - width // 2
                cy = y - height // 2
                
                # Convert to polar coordinates
                r = math.sqrt(cx * cx + cy * cy)
                angle = math.atan2(cy, cx) + rotation
                
                # Create spiral pattern
                spiral_value = math.sin(r * 0.1 + angle * 3) * 0.5 + 0.5
                
                # Color based on position and time
                red = int(255 * (math.sin(angle + rotation) * 0.5 + 0.5) * spiral_value)
                green = int(255 * (math.sin(angle + rotation + 2.09) * 0.5 + 0.5) * spiral_value)
                blue = int(255 * (math.sin(angle + rotation + 4.18) * 0.5 + 0.5) * spiral_value)
                
                frame_data.extend([red, green, blue])
        
        bmp_data = create_bmp_frame(width, height, frame_data)
        frames.append((f"spiral_{frame_num:02d}.bmp", bmp_data))
    
    return frames

def create_wave_animation():
    """Create a sine wave animation"""
    width, height = 300, 100
    frames = []
    num_frames = 20
    
    for frame_num in range(num_frames):
        frame_data = []
        
        # Wave phase
        phase = (frame_num / num_frames) * 2 * math.pi
        
        for y in range(height):
            for x in range(width):
                # Calculate wave
                wave_y = height // 2 + int(20 * math.sin(x * 0.05 + phase))
                
                # Distance from wave line
                dist_from_wave = abs(y - wave_y)
                
                if dist_from_wave <= 2:
                    # Wave line
                    red, green, blue = 255, 255, 0
                elif dist_from_wave <= 5:
                    # Wave glow
                    intensity = 1 - (dist_from_wave - 2) / 3
                    red = int(255 * intensity)
                    green = int(255 * intensity)
                    blue = int(100 * intensity)
                else:
                    # Background
                    red = int(20 + (y / height) * 50)
                    green = int(30 + (y / height) * 70)
                    blue = int(100 + (y / height) * 100)
                
                frame_data.extend([red, green, blue])
        
        bmp_data = create_bmp_frame(width, height, frame_data)
        frames.append((f"wave_{frame_num:02d}.bmp", bmp_data))
    
    return frames

def save_frames(frames, directory):
    """Save frames to directory"""
    os.makedirs(directory, exist_ok=True)
    
    for filename, data in frames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "wb") as f:
            f.write(data)
    
    print(f"Created {len(frames)} frames in '{directory}' directory")

def create_conversion_script():
    """Create a script to convert all animations to GIF"""
    script_content = """#!/bin/bash
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
"""
    
    with open("convert_all.sh", "w") as f:
        f.write(script_content)
    
    os.chmod("convert_all.sh", 0o755)
    print("Created convert_all.sh script")

def main():
    print("Advanced GIF Animation Generator")
    print("=" * 40)
    
    # Create different animations
    print("\nGenerating bouncing ball animation...")
    bounce_frames = create_bouncing_ball_animation()
    save_frames(bounce_frames, "bounce_frames")
    
    print("\nGenerating spiral animation...")
    spiral_frames = create_spiral_animation()
    save_frames(spiral_frames, "spiral_frames")
    
    print("\nGenerating wave animation...")
    wave_frames = create_wave_animation()
    save_frames(wave_frames, "wave_frames")
    
    # Create conversion script
    create_conversion_script()
    
    print("\nTo convert all animations to GIF, run:")
    print("  ./convert_all.sh")
    print("\nOr convert individual animations:")
    print("  convert bounce_frames/*.bmp -delay 8 -loop 0 bouncing_ball.gif")
    print("  convert spiral_frames/*.bmp -delay 12 -loop 0 colorful_spiral.gif")
    print("  convert wave_frames/*.bmp -delay 15 -loop 0 sine_wave.gif")

if __name__ == "__main__":
    main()