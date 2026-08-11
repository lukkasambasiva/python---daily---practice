#sum of even and odd numbers
num=123456
s1=0
s2=0
while num>0:
     d = num%10
     if d%2==0:
        s1+=d
     else:
         s2+=d
     num=num//10
print('Even :',s1)
print('Odd :',s2)
