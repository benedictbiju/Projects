import os
import tkinter as tk
from PIL import ImageTk
#create a window 
window = tk.Tk()

#name the window
window.title("To-Do List")

#to adjust the position of the window
window.eval("tk::PlaceWindow . center")

#edit the frame of the window
frame1 = tk.Frame(window, width = 700, height = 800, bg = "#C9DFE3")
frame1.grid(row = 0, column = 0)

#to add logo (use script-relative path so running from any CWD works)
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "Assets", "todologo.png")
logo_img = ImageTk.PhotoImage(file=logo_path)
logo_widget = tk.Label(frame1, image=logo_img, bg = "#C9DFE3")
logo_widget.image = logo_img
logo_widget.pack()

#activate the window
window.mainloop()   