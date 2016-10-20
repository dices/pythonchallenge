import os
import zipfile
import re
filename = '90052.txt'
commentList = b''
while(True):
    with zipfile.ZipFile('channel.zip') as z:
        fileinfo = z.getinfo(filename)
        print (fileinfo.comment)
        commentList += fileinfo.comment
        with z.open(filename) as f:
            for line in f:
                print(line)
                m = re.search(r"Next nothing is (\d+)$", line.decode("utf8"))
                if m:
                    filename = m.group(1)+'.txt'
                else:
                    print(commentList.decode())
                    exit()

