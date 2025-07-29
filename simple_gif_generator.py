#!/usr/bin/env python3
"""
Simple GIF Animation Generator
This script demonstrates different ways to create GIF animations.
"""

import os
import sys

def check_dependencies():
    """Check what image libraries are available"""
    available = {}
    
    try:
        from PIL import Image, ImageDraw, ImageFont
        available['PIL'] = True
        print("✓ PIL/Pillow is available")
    except ImportError:
        available['PIL'] = False
        print("✗ PIL/Pillow not available")
    
    try:
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation
        available['matplotlib'] = True
        print("✓ Matplotlib is available")
    except ImportError:
        available['matplotlib'] = False
        print("✗ Matplotlib not available")
    
    try:
        import imageio
        available['imageio'] = True
        print("✓ imageio is available")
    except ImportError:
        available['imageio'] = False
        print("✗ imageio not available")
    
    return available

def create_ascii_animation():
    """Create a simple ASCII animation that can be displayed in terminal"""
    frames = [
        "●○○○○",
        "○●○○○", 
        "○○●○○",
        "○○○●○",
        "○○○○●",
        "○○○●○",
        "○○●○○",
        "○●○○○"
    ]
    
    print("ASCII Animation Preview:")
    print("=" * 20)
    
    import time
    for i in range(3):  # 3 cycles
        for frame in frames:
            print(f"\r{frame}", end="", flush=True)
            time.sleep(0.2)
    print("\n" + "=" * 20)

def create_simple_ppm_frames():
    """Create simple PPM image frames that can be converted to GIF"""
    width, height = 100, 100
    frames = []
    
    for frame_num in range(20):
        # Create a simple animation - moving circle
        frame_data = []
        
        # Calculate circle position
        center_x = int(50 + 30 * (frame_num / 19.0 - 0.5))
        center_y = 50
        radius = 10
        
        for y in range(height):
            row = []
            for x in range(width):
                # Distance from center
                dist = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                
                if dist <= radius:
                    # Inside circle - red
                    row.extend([255, 0, 0])
                else:
                    # Outside circle - white
                    row.extend([255, 255, 255])
            
            frame_data.extend(row)
        
        # Create PPM content
        ppm_content = f"P6\n{width} {height}\n255\n"
        ppm_bytes = ppm_content.encode() + bytes(frame_data)
        
        frames.append((f"frame_{frame_num:02d}.ppm", ppm_bytes))
    
    return frames

def save_ppm_frames(frames):
    """Save PPM frames to files"""
    os.makedirs("animation_frames", exist_ok=True)
    
    for filename, data in frames:
        filepath = os.path.join("animation_frames", filename)
        with open(filepath, "wb") as f:
            f.write(data)
    
    print(f"Created {len(frames)} PPM frames in 'animation_frames' directory")

def create_html_animation():
    """Create an HTML file with CSS animation as an alternative to GIF"""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>CSS Animation Alternative to GIF</title>
    <style>
        body {
            margin: 0;
            padding: 50px;
            background: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        
        .container {
            width: 400px;
            height: 200px;
            background: white;
            border: 2px solid #333;
            position: relative;
            overflow: hidden;
            margin: 20px 0;
        }
        
        .moving-circle {
            width: 40px;
            height: 40px;
            background: #ff4444;
            border-radius: 50%;
            position: absolute;
            top: 80px;
            animation: moveCircle 2s ease-in-out infinite alternate;
        }
        
        @keyframes moveCircle {
            0% { left: 10px; }
            100% { left: 350px; }
        }
        
        .bouncing-ball {
            width: 30px;
            height: 30px;
            background: #4444ff;
            border-radius: 50%;
            position: absolute;
            left: 50%;
            animation: bounce 1s ease-in-out infinite;
        }
        
        @keyframes bounce {
            0%, 100% { top: 150px; }
            50% { top: 20px; }
        }
        
        .rotating-square {
            width: 50px;
            height: 50px;
            background: #44ff44;
            position: absolute;
            top: 75px;
            left: 175px;
            animation: rotate 2s linear infinite;
        }
        
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .pulse-circle {
            width: 60px;
            height: 60px;
            background: #ff44ff;
            border-radius: 50%;
            position: absolute;
            top: 70px;
            left: 270px;
            animation: pulse 1.5s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.5); opacity: 0.5; }
        }
    </style>
</head>
<body>
    <h1>Animated Elements (GIF Alternative)</h1>
    
    <h2>Moving Circle</h2>
    <div class="container">
        <div class="moving-circle"></div>
    </div>
    
    <h2>Bouncing Ball</h2>
    <div class="container">
        <div class="bouncing-ball"></div>
    </div>
    
    <h2>Multiple Animations</h2>
    <div class="container">
        <div class="rotating-square"></div>
        <div class="pulse-circle"></div>
    </div>
    
    <p>These CSS animations can be converted to GIF using screen recording tools or browser automation.</p>
</body>
</html>"""
    
    with open("animation_demo.html", "w") as f:
        f.write(html_content)
    
    print("Created 'animation_demo.html' - open in browser to see animations")

def main():
    print("GIF Animation Generator")
    print("=" * 30)
    
    # Check what's available
    deps = check_dependencies()
    
    print("\nCreating animations...")
    
    # ASCII animation in terminal
    create_ascii_animation()
    
    # Create PPM frames (can be converted to GIF with external tools)
    print("\nGenerating image frames...")
    frames = create_simple_ppm_frames()
    save_ppm_frames(frames)
    
    # Create HTML animation as alternative
    create_html_animation()
    
    print("\nGenerated content:")
    print("1. ASCII animation (displayed above)")
    print("2. PPM image frames in 'animation_frames/' directory")
    print("3. HTML animation in 'animation_demo.html'")
    
    print("\nTo convert PPM frames to GIF (if you have ImageMagick):")
    print("  convert animation_frames/*.ppm -delay 10 -loop 0 animation.gif")
    
    print("\nTo convert PPM frames to GIF (if you have ffmpeg):")
    print("  ffmpeg -r 10 -i animation_frames/frame_%02d.ppm -y animation.gif")

if __name__ == "__main__":
    main()