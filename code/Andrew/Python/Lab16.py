
from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here
        y = int(0.299*r + 0.587*g + 0.114*b)

        pixels[i, j] = (y, y, y)

img.show()