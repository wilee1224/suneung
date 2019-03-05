import os
import time
import keyboard
from pynput.mouse import Controller
import pyscreenshot as ImageGrab
from tkinter import filedialog
from tkinter import *

mouse = Controller()
global cap

def openPDF(filename, filepath, year, month):
    os.startfile(filename)
    time.sleep(3)
    keyboard.press_and_release('ctrl+l')
    time.sleep(2)
    keyboard.press_and_release('ctrl+y')
    keyboard.write('200')
    keyboard.press('ENTER')

    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0
    i = 0

    while True:

        # cap = []
        q1 = keyboard.is_pressed('1')
        q2 = keyboard.is_pressed('2')
        quit = keyboard.is_pressed('z')
        if quit == True:
            break

        if q1 == True:
            tmp1 = get_position()[0]
            tmp2 = get_position()[1]
            # cap.append(0)
            # cap.append(0)

        if q2 == True:
            tmp3 = tmp1 + 1000
            tmp4 = get_position()[1]
        # cap.append(tmp1)
        # cap.append(tmp2)
        # cap.append(tmp3)
        # cap.append(tmp4)
            im = ImageGrab.grab(bbox=(tmp1, tmp2, tmp3, tmp4))
            i +=1
            im.save('{0}/{1}_{2}_{3}.png'.format(filepath, year, month, i))

        # print(cap)

def get_position():
        array = []
        array.append((mouse.position)[0])
        array.append((mouse.position)[1])
        return array

def fileSelect():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("pdf files","*.pdf"),("all files", "*.*")))
    print(root.filename)
    basename = os.path.basename(root.filename)
    year = basename[:4]
    month = basename[4:6]
    print(year, month)
    filepath = os.path.dirname(root.filename)
    print(filepath)
    openPDF(root.filename, filepath, year, month)

if __name__ == '__main__':
    fileSelect()
