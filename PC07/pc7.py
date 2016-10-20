from PIL import Image

im = Image.open("oxygen.png")  # Can be many different formats.
pix = im.load()
width, height = im.size
for i in range(0,height):
    for j in range(0,width,7):
        print(chr(im.getpixel((j,48))[0]),end="")
    print()
#print(pix[x, y])
  # Get the RGBA Value of the a pixel of an image
#pix[x, y] = value  # Set the RGBA Value of the image (tuple)

for c in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    print(chr(c),end="")