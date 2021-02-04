# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("hello")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import Tkinter

def my_window(w, h):
  ws = root.winfo_screenwidth()
  hs = root.winfo_screenheight()
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)
  root.geometry("%dx%d+%d+%d" % (w, h, x, y))

root = Tkinter.Tk(className='python windows app')
my_window(500, 500)
root.mainloop()