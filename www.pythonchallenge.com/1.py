'http://www.pythonchallenge.com/pc/def/map.html'

old_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
x = 'yzabcdefghijklmnopqrstuvwx'
y = 'abcdefghijklmnopqrstuvwxyz'
my_table = old_string.maketrans(x, y)
new_string = old_string.translate(my_table)
print(new_string)

problem = 'map'
solution = problem.translate(my_table)
print(solution)


my_solution = 'http://www.pythonchallenge.com/pc/def/ocr.html'