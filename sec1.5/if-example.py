name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12: 
    print('you are not Alice kiddo')
elif age > 2000:
    print('unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alice, granny')


#Truthy and Elsey Statements

#bad formatting
print('Enter a name')
name = input()
if name:
    print('Thank you for entering a name')
else: 
    print('You did not enter a name')

#good formatting
print('Enter a name')
name = input()
if name != '':
    print('Thank you for entering a name')
else: 
    print('You did not enter a name')

