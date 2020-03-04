# section 1.8 recap


## For loops

<li>
On OS X for installing modules use...
</li>

```
pip3 install ModuleName
```

<li>
Must have modules to run specific functions. 
</li>
<li>
To terminate some code...

```
>>> import sys
>>> sys.exit()
```
</li>
<li>
Then in editor...

```
import sys 
print('Hello')
sys.exit()
print('Goodbye')
```
Everything after sys.exit() will not execute
</li>


<li>
in the shell...
</li>

```
>>> import random
>>> random.randint(1, 100)
79
```
<li> 
Pyperclip example use in the shell
</li>

```
>>> pyperclip.copy('hi there')
>>> pyperclip.paste()
'hi there'
>>> 
```
## Other Modules

pip3 install send2trash

pip3 install requests

pip3 install beautifulsoup4

pip3 install selenium

pip3 install openpyxl==2.1.4

pip3 install PyPDF2

pip3 install python-docx (install python-docx, not docx)

pip3 install imapclient

pip3 install pyzmail

pip3 install twilio

pip3 install pillow

pip3 install pyobjc-core (on OS X only)

pip3 install pyobjc (on OS X only)

pip3 install python3-xlib (on Linux only)

pip3 install pyautogui
