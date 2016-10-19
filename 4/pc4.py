import urllib.request
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
target='8022'
while(target != ""):
    print( url+target)
    with urllib.request.urlopen(url+target) as response:
        html = response.read()
        print(html)
        m = re.search(r"and the next nothing is (\d+)$", html.decode("utf8"))
        if m:
            target = m.group(1)
        else:
            target = ""



