import os
import time
import keyboard
from pynput.mouse import Listener
import pyscreenshot as ImageGrab
from tkinter import filedialog
from tkinter import *

class Suneung:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def mouseEvent(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()
        return self.x1, self.y1, self.x2, self.y2

    def on_click(self, x, y, button, pressed):
        if pressed:
            print('pressed', (x,y))
            self.x1 = x
            self.y1 = y
        else:
            print('Released', (x,y))
            self.x2 = x
            self.y2 = y
        if not pressed:
            return False

def openPDF(filename):
    os.startfile(filename)
    time.sleep(3)
    keyboard.press_and_release('ctrl+l')
    s = Suneung()
    t = s.mouseEvent()
    im = ImageGrab.grab(bbox=(t[0], t[1], t[2],t[3]))
    im.show()

def fileSelect():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("pdf files","*.pdf"),("all files", "*.*")))
    print(root.filename)
    basename = os.path.basename(root.filename)
    year = basename[:4]
    month = basename[5:6]

    openPDF(root.filename)

if __name__ == '__main__':
    fileSelect()