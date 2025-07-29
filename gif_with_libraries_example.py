#!/usr/bin/env python3
"""
GIF Generation with Python Libraries
Examples of how to create GIFs when popular libraries are available
"""

def create_gif_with_pillow():
    """Example using PIL/Pillow library"""
    try:
        from PIL import Image, ImageDraw
        
        # Create frames
        frames = []
        width, height = 200, 200
        
        for i in range(20):
            # Create new image with white background
            img = Image.new('RGB', (width, height), 'white')
            draw = ImageDraw.Draw(img)
            
            # Draw animated circle
            angle = (i / 20) * 360
            x = 100 + 50 * (i / 19)
            y = 100 + 30 * ((i / 19) - 0.5)
            
            # Draw circle with changing color
            color = (255 - i * 10, i * 12, 100 + i * 5)
            draw.ellipse([x-20, y-20, x+20, y+20], fill=color)
            
            frames.append(img)
        
        # Save as GIF
        frames[0].save(
            'pillow_animation.gif',
            save_all=True,
            append_images=frames[1:],
            duration=100,
            loop=0
        )
        
        print("Created pillow_animation.gif using PIL/Pillow")
        return True
        
    except ImportError:
        print("PIL/Pillow not available")
        return False

def create_gif_with_matplotlib():
    """Example using matplotlib"""
    try:
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation
        import numpy as np
        
        # Set up the figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_xlim(0, 2*np.pi)
        ax.set_ylim(-2, 2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Animated Sine Wave')
        
        # Create empty line objects
        line1, = ax.plot([], [], 'b-', linewidth=2, label='sin(x)')
        line2, = ax.plot([], [], 'r-', linewidth=2, label='cos(x)')
        ax.legend()
        
        # Animation function
        def animate(frame):
            x = np.linspace(0, 2*np.pi, 100)
            phase = frame * 0.1
            y1 = np.sin(x + phase)
            y2 = np.cos(x + phase)
            
            line1.set_data(x, y1)
            line2.set_data(x, y2)
            return line1, line2
        
        # Create animation
        anim = animation.FuncAnimation(
            fig, animate, frames=60, interval=50, blit=True, repeat=True
        )
        
        # Save as GIF
        anim.save('matplotlib_animation.gif', writer='pillow', fps=20)
        plt.close()
        
        print("Created matplotlib_animation.gif using matplotlib")
        return True
        
    except ImportError:
        print("Matplotlib not available")
        return False

def create_gif_with_imageio():
    """Example using imageio library"""
    try:
        import imageio
        import numpy as np
        
        # Create frames
        frames = []
        width, height = 150, 150
        
        for i in range(30):
            # Create frame as numpy array
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Create rotating pattern
            center_x, center_y = width // 2, height // 2
            angle = (i / 30) * 2 * np.pi
            
            for y in range(height):
                for x in range(width):
                    # Distance from center
                    dx = x - center_x
                    dy = y - center_y
                    dist = np.sqrt(dx*dx + dy*dy)
                    
                    # Create rotating color pattern
                    pixel_angle = np.arctan2(dy, dx) + angle
                    
                    if dist < 60:
                        frame[y, x, 0] = int(127 + 127 * np.sin(pixel_angle))
                        frame[y, x, 1] = int(127 + 127 * np.sin(pixel_angle + 2.09))
                        frame[y, x, 2] = int(127 + 127 * np.sin(pixel_angle + 4.18))
                    else:
                        frame[y, x] = [50, 50, 50]  # Gray background
            
            frames.append(frame)
        
        # Save as GIF
        imageio.mimsave('imageio_animation.gif', frames, duration=0.1)
        
        print("Created imageio_animation.gif using imageio")
        return True
        
    except ImportError:
        print("imageio not available")
        return False

def create_installation_guide():
    """Create a guide for installing required libraries"""
    guide = """
# GIF Animation with Python Libraries

## Installation Commands

### For PIL/Pillow:
```bash
pip install Pillow
```

### For matplotlib:
```bash
pip install matplotlib
```

### For imageio:
```bash
pip install imageio
```

### For all at once:
```bash
pip install Pillow matplotlib imageio numpy
```

## Usage Examples

### 1. PIL/Pillow (Recommended for simple animations)
- Best for: Simple shapes, text, basic graphics
- Pros: Lightweight, easy to use, direct GIF support
- Cons: Limited to basic drawing operations

### 2. Matplotlib (Best for data visualization)
- Best for: Plots, charts, scientific visualizations
- Pros: Excellent for data plots, many animation features
- Cons: Larger file sizes, slower for simple graphics

### 3. imageio (Best for array-based animations)
- Best for: Working with numpy arrays, image processing
- Pros: Fast, flexible, works well with numpy
- Cons: Requires numpy knowledge

## Tips for Better GIFs:
1. Keep frame count reasonable (20-60 frames)
2. Optimize colors (use palette mode when possible)
3. Set appropriate duration/fps
4. Consider file size vs quality tradeoffs
5. Use loop=0 for infinite looping
"""
    
    with open("gif_libraries_guide.md", "w") as f:
        f.write(guide)
    
    print("Created gif_libraries_guide.md")

def main():
    print("GIF Generation with Python Libraries")
    print("=" * 40)
    
    # Try each library
    pillow_success = create_gif_with_pillow()
    matplotlib_success = create_gif_with_matplotlib()
    imageio_success = create_gif_with_imageio()
    
    # Create installation guide
    create_installation_guide()
    
    print("\nSummary:")
    print(f"PIL/Pillow: {'✓' if pillow_success else '✗'}")
    print(f"Matplotlib: {'✓' if matplotlib_success else '✗'}")
    print(f"imageio: {'✓' if imageio_success else '✗'}")
    
    if not any([pillow_success, matplotlib_success, imageio_success]):
        print("\nNo libraries available. Install them with:")
        print("pip install Pillow matplotlib imageio numpy")
    
    print("\nCheck gif_libraries_guide.md for detailed installation and usage instructions.")

if __name__ == "__main__":
    main()