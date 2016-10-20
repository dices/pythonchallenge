from itertools import groupby
def lookandsay(number):
    return ''.join(str(len(list(g))) + k
                   for k, g in groupby(number))

numberstring = 'PC01'
for i in range(30):
    print(numberstring)
    numberstring = lookandsay(numberstring)

print(len(numberstring))