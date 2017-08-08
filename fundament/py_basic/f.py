from functools import reduce


def str2float(s):
    r=s.split('.')
    #l=r[0]
    #i=r[1]
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x, y: x * 0.1+ y  , map(char2num, r[1][::-1]))/10
print('str2float(\'123.456\') =',str2float('123.456'))
