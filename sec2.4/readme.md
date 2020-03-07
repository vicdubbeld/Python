# Section 2.4 recap

## For loops with lists


```
>>> for i in range(4):
...     print(i)
... 
0
1
2
3
```
```
>>> range(4)
range(0, 4)
>>> [0, 1, 2, 3]
[0, 1, 2, 3]
>>> for i in [0, 1, 2, 3]:
...     print(i)
... 
0
1
2
3
```
Similar concept to js...

```
>>> list = [0, 1, 2, 3, 4]
>>> for i in list:
...     print(i)
... 
0
1
2
3
4
```
Handling strings...
```
>>> supplies = ['pens', 'staplers', 'paper', 'binder']
>>> for i in range(len(supplies)):
...     print(str(i) + ' in the list is: ' + supplies[i]) 
... 
0 in the list is: pens
1 in the list is: staplers
2 in the list is: paper
3 in the list is: binder
```
W/out augmented assignment operators +=

```
>>> spam = 42
>>> spam = spam + 1
43
```
With augmented assignment operators +=

```
>>> spam += 1 
```
