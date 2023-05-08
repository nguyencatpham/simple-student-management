import tkinter as tk
from gui.introduce.gui import introduceWindow
from gui.main_window.main import mainWindow

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    introduceWindow()

    root.mainloop()
