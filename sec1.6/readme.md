# section 1.6 recap


## While loops

<li>
While loops iterate and then go back to start of while statement to check the condition and execute until condition is false.
</li>
<li>
At end of an if block, the program execution continues on with the rest of the program.
</li>
<li>
Use 'break' statements to immediately jump out of the loop and not check condition again. Goes to next line.
</li>
<li>
Use 'continue' statements to cause the execution to jump back to the start of the loop and re-check the condition.
</li>

```
If name == 'your name':
    break
print('thank you')
```
```
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
```
