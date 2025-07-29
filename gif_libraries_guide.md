
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
