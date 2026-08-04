#simple interest
'''principle p
rate
time

step1: remember priciple amount
step2: remember interest rate
step3: remember time
step4: caluclte simple intrest
step5:  final amount to pay'''

p =float(input("Enter the Priciple Amount :"))#10,000
r =float(input("Enter the rate of Interest:"))#10.0
t = float(input("Enter the Time duration:"))#2 years
si =(p*r*t)/100 #si=10000*10.*24
total_amount= p+si
print("simple interest",si)
print("Total Amount to Pay",total_amount)
