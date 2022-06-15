from time import sleep as thread_sleep
import threading
from pynput import mouse
from pynput.mouse import Button, Controller
from pynput import keyboard
from pynput.keyboard import KeyCode, Key

# clicks per second
rate = 20
# whether clicker is toggled or not
should_click = False
# kill trigger
# TODO: you should be able to press escape to change this to true
done = False

def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    global should_click
    if not pressed and button == Button.middle:
        print(f'{button} released')
        should_click = not should_click

def on_scroll(x, y, dx, dy):
    pass

# object for listening for input
listener = mouse.Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll)
listener.start()

# object for inputting clicks
controller = Controller()

# keep looping until kill switch is pressed
while not done:
    if should_click:
        # press and unpress mouse left
        controller.press(Button.left)
        controller.release(Button.left)
        print('clicked')
        # 1 / rate is delay
    thread_sleep(1/rate)

listener.stop()
