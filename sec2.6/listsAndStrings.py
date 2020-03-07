def eggs(someParameter): #all this eggs function does is call the append method
    someParameter.append('Hello') 


spam = [1, 2, 3]

eggs(spam)
print(spam) # >>> [1, 2, 3, 'Hello']

