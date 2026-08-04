#super market  billing system

name=input('Enter A name :')#samba
amount=float(input('Enter a amount :'))#6000
m_ship=input('Do you have Membership (yes/No):')#yes
coupon=input('Do you have Coupon (yes/No):')#no
org_amount = amount
if amount>5000:#6000>5000
   amount = amount-amount*0.1#6000-6000*0.1=5400
if  m_ship=='yes':#yes
   amount = amount-amount*0.05#5400-5400*0.05=5130
if coupon=='yes':
   amount = amount-amount*0.05
gst = amount*0.18#5130+0.18=6053
amount = amount + gst
print('Customer Name',name)
print('Original Bill',org_amount)
print('Final Bill',round(amount, 2))
