from pynput.mouse import Controller
import keyboard

mouse = Controller()

def get_position():
    i = 0
    while True:
        array = []
        q = keyboard.is_pressed('q')
        if q == True:
            print('q is pressed')
            i += 1
            print(i)
            if i==1:
                print('#')
                array.append((mouse.position)[0])
                array.append((mouse.position)[1])
                print(array)
                i = 0
            if i > 1:
                return 0
        continue

if __name__ == '__main__':
    get_position()




