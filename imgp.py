from PIL import ImageGrab

img = ImageGrab.grab()
pixels = img.load()
width, height = img.size
coords = []
for x in range(width):
    for y in range(height):
        print(pixels[x,y])