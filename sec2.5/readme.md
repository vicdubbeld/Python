# 2.5 Recap

## Methods


Index is the name of the method.
```
>>> spam = ['hi', 'howdy', 'hello']
>>> spam.index ('hello')
2
```
Below does not work because Python does not know which list you are referring to
```
>>> index('hello') 
Traceback (most recent call last)...
```

Will return first time item occurred in list
```
>>> spam = ['Pooka', 'Cat', 'Pooka']
>>> spam.index('Pooka')
0
>>> 

```
Use append argument to add item to list...

```
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
```

To remove items from list

```
>>> spam = ['bat', 'cat', 'dog', 'bat']
>>> spam.remove('bat')
>>> spam
['cat', 'dog', 'bat']

```
The remove method will only delete the first time the item occurred. The delete method will delete by index. Going off of the above list...

```
>>> del spam[0]
>>> spam
['dog', 'bat']
```
The sort method will sort a list of strings/integers that were in random order.

```
>>> spam = ['dogs', 'cats', 'ants', 'bats']
>>> spam.sort()
>>> spam
['ants', 'bats', 'cats', 'dogs']
```