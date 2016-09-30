>>> import re
>>> m = re.search("output_(\d{4})", "output_1986.txt")
>>> print(m.group(1))
1986
>>> print(m.group(0))
output_1986


>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
