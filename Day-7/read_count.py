#read number and count
num=int(input('Enter a number:'))
c=0
s1=0
s2=0
while num>0:
    c+=1
    d=num%10
    if d%2==0:
        s1+=1
    else:
        s2+=1
    num//=10
print('Total digits :',c)
print('Even digits :',s1)
print('Odd digits :',s2)
