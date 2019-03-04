from pynput.mouse import Controller
import keyboard

def get_position(self):
    print('q is pressed')
    array = []
    i = 0
    if i==0:
        print('#')
        array.append((mouse.position)[0])
        array.append((mouse.position)[1])
        i += 1
        # print(array)
        return array
    elif i > 0: return
    # if i == 2:
    #     print('##')
    #     array.append((mouse.position)[0])
    #     array.append((mouse.position)[1])
    #     print(array)
    #     i = 0
    #     continue

if __name__ == '__main__':
    while True:
        q = keyboard.is_pressed('q')
        if q == True:
            print(get_position())
        else :
            continue



