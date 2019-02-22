import os
import time
import keyboard
from pynput.mouse import Listener



# mouse  = Controller

def openPdf():
    f = open("수학(가형)_홀.pdf")
    os.startfile("수학(가형)_홀.pdf")
    time.sleep(3)
    keyboard.press_and_release('ctrl+l')

    with Listener(on_click=on_click) as listener:
        listener.join()
    f.close()

def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    print(type({1}))
    global x1
    x1 = x
    print('x1 : ', x1)

    print('{0},{1}'.format('pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        global x2
        x2 = x
        print('x1 : ', x1)
        print('x2 : ', x2)
        # Stop listener
        x3 = (x1+x2)/2
        print('x3 : ', x3)
        return False


# Collect events until released


if __name__ == '__main__':
    openPdf()