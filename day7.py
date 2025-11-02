import tkinter as tk
# Create window

window = tk.Tk()
window.title("My First App")
window.geometery("300x200")


# Add a label
label = tk.Label(window, text="Hello, world!")
label.pack()

# Add a button
def say_hi():
    label.config(text="hi there!")

    button = tk.Button(window, text="click me", command=say_hi)
    window.mainloop()
