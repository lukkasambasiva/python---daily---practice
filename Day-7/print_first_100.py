#print the first 100 prime numbers
num=2
c=0
while True:
    d=2
    while d<=num//2:
        if num%d==0:
            break
        d+=1
    else:
        print(num)
        c+=1
        if c==100:
            break
    num+=1
