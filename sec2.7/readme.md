# Sec.2.7 Dictionary Data Type
<li>
Dictionaries contain key-value pairs. Keys are like a list's indexes.
</li>
<li>
Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
</li>

```
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud' }
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur'
'My cat has gray fur'
```
Dictionaries can still use integer values too...

```
>>> spam = {12345: 'Luggage combination', 42: 'The Answer'}
```
Dictionaries are unordered, unlike lists. So there is no first item in a dictionary.
```
>>> [1, 2, 3] == [3, 2, 1]
False
```
To check for items...

```
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
>>> eggs == ham
True
>>> 'name' in eggs
True
```
## Keys(), values(), and items() Dictionary methods

```
>>> list(eggs.keys())
['name', 'species', 'age']
>>> list(eggs.values())
['Zophie', 'cat', 8]
>>> list(eggs.items())
[('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
```

## For loops


```
>>> for k in eggs.keys():
        print(k)
 
name
species
age

>>> for v in eggs.values():
        print(v)
 
Zophie
cat
8
```
Can use multiple assignment trick to have multiple variables in for loop
```
>>> for k, v in eggs.items():
...     print(k, v)
... 
name Zophie
species cat
age 8
```
## get() method

This can return a default value if a key doesn't exist.
2 arguments (key, fallback default value)
```
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs.get('age', 0)
8
```
8 was returned of course because it was there, however if it were not then 0 would have been returned.

## setdefault() method

This is the opposite of the get() method. It can set a value if a key doesn't exist.

```
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs.setdefault('color', 'black')
'black'
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
```
You cannot change the color to 'orange' with this. 

## pprint module

This module's pprint() function returns a string value of this output.

### Running data.py
Let's count how many characters are in this sentence:
<li>
'It was a bright cold day in April, and the clocks were striking thirteen'
</li>

```
{' ': 13,
 ',': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
```
The possibilities are endless here. You could literally put an entire book's text here and it will run the program.