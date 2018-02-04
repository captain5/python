def consumer():
    k = '123'
    print(k)
    while True:
        k = '100 OK'
        n = yield k
        if not n:
            print("111")
            return
        print('[CONSUMER] Consuming %s...' % n)
        k = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 1:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)