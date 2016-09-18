fn = 'test.txt'
file(fn, 'w+').write('test\ntest2')
content = file(fn, 'r').read()
print content.replace('\r', '\\r').replace('\n', '\\n')
