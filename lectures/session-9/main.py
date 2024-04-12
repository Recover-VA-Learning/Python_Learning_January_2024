import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        f1 = tk.Frame(width=200, height=200, background="red")
        f2 = tk.Frame(width=100, height=100, background="blue")

        f1.pack(fill="both", expand=True, padx=20, pady=20)
        f2.place(in_=f1, anchor="c", relx=.5, rely=.5)

        self.entrythingy = tk.Entry()
        self.entrythingy.pack(in_=f2)

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
root.geometry("400x400")

myapp = App(root)
myapp.mainloop()