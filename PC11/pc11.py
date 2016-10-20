from PIL import Image
im = Image.open('cave.jpg')

pixels = list(im.getdata())
width, height = im.size
a = pixels[::2]
b = pixels[1::2]
#print(type(pixels))
#print(pixels[1])
#a,b = zip(*pixels)
#a,b = map(list(zip(*pixels)))
im2 = Image.new(im.mode, (width,height))
im2.putdata(a)
im2.show()