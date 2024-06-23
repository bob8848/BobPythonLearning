# simple_gui.py
import tkinter as tk

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI")

        self.label = tk.Label(root, text="Hello, World!")
        self.label.pack()

        self.button = tk.Button(root, text="Click Me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SimpleGUI(root)
    root.mainloop()
