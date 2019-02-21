import os
import time
import keyboard
from pynput.mouse import Listener

# mouse  = Controller


def openPdf():
    # f = open("수학(가형)_홀.pdf")
    # os.startfile("수학(가형)_홀.pdf")
    # time.sleep(3)
    # keyboard.press_and_release('ctrl+l')
    with Listener(on_click=on_click) as listener:
        listener.join()
    # print(clicked[0], clicked[1], clicked[2], clicked[3])
    # f.close()
    print('firstClick : ', clicked)

def on_click(x, y, button, pressed):
    global clicked
    clicked = []
    if pressed:
        clicked.append('{0},{1}'.format(x,y))
        clicked.append('{0}'.format(y))

    print('{0},{1}'.format('pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        clicked.append('{0}'.format(x))
        clicked.append('{0}'.format(y))
        return False

if __name__ == '__main__':

    openPdf()