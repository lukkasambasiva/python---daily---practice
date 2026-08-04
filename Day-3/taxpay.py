income=int(input('Enter your annual income :'))
if income>50000:
    tax=income*0.05
elif income>100000:
    tax=income*0.1
elif income>200000:
    tax=income*0.2
elif income>300000:
    tax=income*0.3
else:
    print('no tax')
print(tax)
