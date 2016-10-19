import pickle

with open('banner.p', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)

for pixel_group in data:
    current_line = ''
    for pixel in pixel_group:
        current_line += pixel[0] * pixel[1]
    print(current_line)