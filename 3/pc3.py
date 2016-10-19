s = ''.join([line.rstrip() for line in open('pc3.dat')])
import re
print(s)
m = re.findall('[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}', s)
print(m) #['l', 'i', 'n', 'k', 'e', 'd', 'l', 'i', 's', 't']
