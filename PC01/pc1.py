#http://www.pythonchallenge.com/pc/def/map.html
import string
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
translate_matrix = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
trans_table = str.maketrans(string.ascii_lowercase, translate_matrix)

print(text.translate(trans_table))
print("map".translate(trans_table))