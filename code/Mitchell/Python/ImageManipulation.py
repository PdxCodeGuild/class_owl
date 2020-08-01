from PIL import Image
import colorsys

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = 0.299*R + 0.587*G + 0.114*B
        h, s, l = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        l = max((.4), l - .5)
        s = max((.4), s - .5)
        
        r, g, b = colorsys.hsv_to_rgb(h, s, l)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = r, g, b

img.show()