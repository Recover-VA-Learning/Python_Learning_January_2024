import tkinter as tk
from tkinter import filedialog

# Use Matplotlib backends for Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import csv
import random

# --- functions ---  # PEP8: `lower_case_names`

def open_file():
    global x
    global y

    file = filedialog.askopenfile(filetypes=[('CSV Files', '*.csv'),
                                             ('Text Files', '*.txt'),
                                             ('All Files', '*.*')])

    if file:
        print('read file')

        x = []
        y = []
        
        reader_csv = csv.reader(file)
        for row in reader_csv:
            x.append(float(row[0]))
            y.append(float(row[1]))

        if x:
            ax.set_xlim(0, 10)
        if y:
            ax.set_ylim(min(y), max(y))
            
        # stop previous animation
        if ani:
            ani._stop()
        #del ani

        # create new animation    
        ani = animation.FuncAnimation(fig, animate, 250, interval=250, blit=False)    
        ani._start()
        
def generate_data():
    global x
    global y
    global ani
    
    print('generate data')
    
    # fake values
    x = list(range(250))
    y = [random.randint(0, 10) for _ in range(250)]

    # 
    if x:
        ax.set_xlim(0, 10)
    if y:
        ax.set_ylim(min(y), max(y))

    # stop previous animation
    if ani:
        ani._stop()
    #del ani

    # create new animation    
    ani = animation.FuncAnimation(fig, animate, 250, interval=250, blit=False)    
    ani._start()
    
def animate(i):
    print('i:', i, x[i:i+10], y[i:i+10])
    
    current_x = x[i:i+10]
    current_y = y[i:i+10]
    
    line.set_xdata(current_x)
    line.set_ydata(current_y)

    if current_x:    
        ax.set_xlim(min(current_x), max(current_x))

    #canvas.draw()
    
    return line,

def stop_animation():
    if ani:
        # matplotlib 3.4.0+   # https://matplotlib.org/3.4.0/gallery/animation/pause_resume.html
        #ani.pause() 
        # older matplotlib 
        ani.event_source.stop()
        if ani._blit:
            for artist in ani._drawn_artists:
                artist.set_animated(False)

def start_animation():
    if ani:
        # matplotlib 3.4.0+   # https://matplotlib.org/3.4.0/gallery/animation/pause_resume.html
        #ani.resume() 
        # older matplotlib 
        ani.event_source.start()
        if ani._blit:
            for artist in ani._drawn_artists:
                artist.set_animated(True)        
            
# --- main ---

# default values at start
x = []
y = []
ani = None

# - GUI -

tk_top = tk.Tk()

file_opener = tk.Button(tk_top, text="Open File", command=open_file)
file_opener.pack()

data_generator = tk.Button(tk_top, text="Generate Data", command=generate_data)
data_generator.pack()

# - empty plot -

try:
    fig = plt.Figure()

    canvas = FigureCanvasTkAgg(fig, master=tk_top)
    canvas.get_tk_widget().pack()

    ax = fig.add_subplot(111)
    line, = ax.plot([], [])
    
    # don't create animation at start
    #ani = animation.FuncAnimation(fig, animate, 250, interval=250, blit=False)    
    #ani.pause()  # it needs newer matplotlib
    
except NameError as ex:
    print(ex)
    
stop = tk.Button(tk_top, text="Stop", command=stop_animation)
stop.pack()

start = tk.Button(tk_top, text="Start", command=start_animation)
start.pack()

print('mainloop')
tk_top.mainloop()