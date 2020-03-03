# section 1.5 recap


## If statements

<li>
Must be indented in a block like so:
</li>

```
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')
```
<li>
Returns
</li>

```
Hi Alice
Done
```
<li>
Elif is the same thing as Else If
In Second Elif statement in if-example, it is not executed because the one before it is true first.
</li>

## Truthy and Falsey Statements
<li>
Basically boolean statements with strings returned in an if else instead of true or false
</li>

<li>
The values 0, 0.0, and the empty string are considered to be Falsey values. When used in conditions they are considered false. 
</li>
<li>
You can always see for yourself which values are Truthy or Falsey by passing them to the bool() function
</li>
