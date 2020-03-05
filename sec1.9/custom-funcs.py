def hello():
    print('Hello')
    print('Hey')
    print('Howdy')

hello()

def goodbye(name):
    print('goodbye ' + name)

goodbye('Alice')
goodbye('Theo')

## More functions...

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)