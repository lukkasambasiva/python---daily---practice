#diffrence bitween big and small
num=int(input('Enter a number :'))
big=0
small=9
while num>0:
    d=num%10
    if d>big:
        big=d
    if d<small:
       small=d
    num//=10
else:
    a=big-small
    print('Diffence value :',a)
