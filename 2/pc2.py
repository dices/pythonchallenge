#http://www.pythonchallenge.com/pc/def/ocr.html
s = ''.join([line.rstrip() for line in open('pc2.dat')])
OCCURRENCES = {}
for c in s: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
avgOC = len(s) // len(OCCURRENCES)
print(''.join([c for c in s if OCCURRENCES[c] < avgOC])  )              # equality