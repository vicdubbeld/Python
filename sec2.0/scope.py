#scope demonstration
#which egg will be printed

def spam():
    eggs = 99 #this 'eggs' gets printed because local scopes cannot use variables in other local scopes
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0 

spam()

