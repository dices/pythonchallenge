s = ''.join([line.rstrip() for line in open('pc3.dat')])
import re
print(s)
m = re.findall('[a-z]{PC01}[A-Z]{PC03}([a-z]{PC01})[A-Z]{PC03}[a-z]{PC01}', s)
print(m) #['l', 'i', 'n', 'k', 'e', 'd', 'l', 'i', 's', 't']
