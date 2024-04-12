## Python GUIs with TKInter

### A few examples of python guis using tkinter
> Read the docs here, https://docs.python.org/3/library/tkinter.html#

Tkinter is installed with modern 3.x+ versions of python and only needs to be imported into script to start using it. Each element is called a "widget" and are customizable (buttons, inputs, labels, etc). A few main widgets:
- Frame: The structure of the appication, you put other this inside the frame
- Buttons: Taking user input
- Checkbuttons: Making selections
- Labels: Display text info
- File Dialogs: Add file to application
- Canvas: Draw something on screen, like a plot

### Examples

- Simple Gui is from the "hello, world" example from tkinter docs- https://docs.python.org/3/library/tkinter.html#a-hello-world-program 

- Calculator Gui is from a tutorial- https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

- Live Plot is from a stackoverflow post- https://stackoverflow.com/questions/71365342/tkinter-moving-graph-created-through-gui-not-from-the-start

### Packaging Python to EXE
- You can move this python to be an executable file with pyinstaller
https://pyinstaller.org/en/stable/

> pip install pyinstaller

There are many parameters that can be set, but if you just want your simple python program packaged you can use this command.

> pyinstaller --onefile -w main.py 

Change main.py to the python file you want to distribute and your exe should be in a "dist" folder in your directory.

