def fib(max):
    if max<2:
        return "max must greater than 2"
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

print('fib(6):')
fib(6)
