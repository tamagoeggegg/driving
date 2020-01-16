country = input('please input your country:')
age = input('please input your age:')
age = int(age)

if country == 'taiwan':
    if age >= 18:
    	print('you can drive')
    else:
    	print('you cannot drive')
elif country == 'America':
    if age >= 16:
    	print('you can drive')
    else:
    	print('you cannot drive')  
