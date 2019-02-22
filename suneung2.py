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
    print('firstClick : ', listx)

def on_click(x, y, button, pressed):
    global clicked
    global a
    global listx
    clicked = ()
    a = int('{0}'.format(x))
    listx = list(clicked)
    listx.append(a)


    # clicked.append('{0}'.format(x))
    # print({1})
    #     return False
    # if pressed:
        # i += 1
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        # global i
        # i = 0
        # global clicked
        # clicked = []
        # print(i)
        # clicked[i] = x
        # i += 1
        # print(i)
        # clicked[i] = y
        # i += 1
        # print(i)

    print('{0},{1}'.format('pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        listx = list(clicked)
        # clicked[i] = x
        # i += 1
        # print(i)
        # clicked[i] = y
        return False


if __name__ == '__main__':

    openPdf()