#Traffic fine
speed = int(input('Enter bike speed :'))
helmet = input('Helmet (Yes/No):')
if speed>100 and helmet=='No':
    print('Fine 5000')
elif speed>100:
    print('Fine 3000')
elif helmet=='No':
    print('Fine 1000')
else:
    print('No Fine')
