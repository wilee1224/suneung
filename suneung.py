import subprocess
import os
import time
import keyboard
import pyHook

def openPdf():
    # subprocess.Popen("수학(가형)_홀.pdf", shell=True)
    # open("수학(가형)_홀.pdf")
    os.startfile("수학(가형)_홀.pdf")
    time.sleep(3)
    keyboard.press_and_release('ctrl+l')


if __name__ == '__main__':
    openPdf()