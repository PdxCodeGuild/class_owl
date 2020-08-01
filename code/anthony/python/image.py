from PIL import Image, ImageOps
import colorsys
import random

img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()


# img = ImageOps.equalize(img)
# img = ImageOps.autocontrast(img)
# img = ImageOps.posterize(img, 1)

# Grayscale
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299*r + 0.587*g + 0.114*b

        pixels[i, j] = r, g, b

gray_image = img.convert("L")
colorized_img = ImageOps.colorize(gray_image, (125, 97, 84), (255, 173, 135))



# Lower brightness
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]

#         h, s, l = colorsys.rgb_to_hsv(r/255, g/255, b/255)

#         l = max(.4, l - .5)

#         r, g, b = colorsys.hsv_to_rgb(h, s, l)

#         r = int(r*255)
#         g = int(g*255)
#         b = int(b*255)

#         pixels[i, j] = r, g, b

# Inverted colors
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]

#         r = 255 - r
#         g = 255 - g
#         b = 255 - b

#         pixels[i, j] = r, g, b



# Create random image
# height, width = 200, 200
# img = Image.new('RGB', (height, width))
# pixels = img.load()


# for x in range(width):
#     for y in range(height):
#         r, g, b = pixels[x, y]

#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)


#         pixels[x, y] = r, g, b



gray_image.show()
colorized_img.show()