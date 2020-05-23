from PIL import Image

im = Image.open("MED.png")
rgb_dict = {}

width, height = im.size
for x in range(width):
    for y in range(height):
        print(x, y)
        color = im.getpixel((x,y))
        if color in rgb_dict:
            rgb_dict[color] += 1
        else:
            rgb_dict[color] = 1

for key in rgb_dict:
    print(str(key) + ": " +  str(rgb_dict[key]))
