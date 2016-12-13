def triangles(max):
    L=[1]
    n=0
    while(n<max):
        yield L
        L.insert(0,1)
        for i in range(1,len(L)-1):
            L[i]+=L[i+1]
        n+=1

for i in triangles(10):
    print(i)
