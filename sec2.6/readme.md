# Sec2.6 Recap
## Lists and Strings


Bunch of different things you can do here...
```
>>> list('hello')
['h', 'e', 'l', 'l', 'o']

>>> name = 'sophie'
>>> name[0]
's'
>>> 'so' in name
True

>>> for letter in name:
...     print(letter)
... 
s
o
p
h
i
e
```
Lists and strings are different in an important way
<li>
lists: Mutable Data Type (can be changed)
</li>
<li>
strings: Immutable Data Type (cannot be changed) can only be replaced by new values
</li>
To properly modify strings is to create a new string using slices...

```
>>> name = 'sophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> newName
'sophie the cat'
```
The true difference between Mutable and Immutable comes up with "references".
Check this out...

```
>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42
```
But here we have a different outcome...

```
>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese[1] = 'Hello'
>>> cheese
[0, 'Hello', 2, 3, 4, 5]
>>> spam
[0, 'Hello', 2, 3, 4, 5]
```

This is because when you assign the list value to spam, Python created this list in the computer's memory and assigned a reference to this list to spam. Even with two different references, they are both the same list.

Passing lists in functions...see .py file

Deep Copy makes brand new list w all the same values
 
 ```
>>> import copy
>>> 
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = copy.deepcopy(spam)
>>> cheese[1] = 42
>>> cheese
['A', 42, 'C', 'D']
>>> spam
['A', 'B', 'C', 'D']
 ```
 This way all the changes you want to make to one list will not interfere with the other list with-originally-the same values.

 Line Continuation - Python understands that below is technically the same line of code. The \ line continuation character can be used to stretch Python instructions across multiple lines.


 ```
>>> spam = ['apples', 
... 'oranges',
... 'bananas',
... 'cats']

>>> print('four score and seven ' + \
... 'years')
four score and seven years
 ```