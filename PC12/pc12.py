from PIL import Image
im = Image.open('evil1.jpg')

pixels = list(im.getdata())
width, height = im.size

a = pixels[::2]
b = pixels[1::2]

im2 = Image.new(im.mode, (width,height))
im2.putdata(a)
im2.show()