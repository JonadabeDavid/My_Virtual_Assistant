from pynput.keyboard import Controller, Key
keyb = Controller()
with keyb.pressed(Key.alt):
    keyb.press(Key.left)
