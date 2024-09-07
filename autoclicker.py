import pyautogui
import time
import keyboard  

clicking = False
x = 0
times = -1  # Change this to the number of times you want it to click (-1 means infinite loop)

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print("Started Clicking")
    else:
        print("Stopped Clicking")

# Register the key combination (Ctrl + Comma)
keyboard.add_hotkey('ctrl+comma', toggle_clicking)

while True:
    if clicking:
        if x == times:
            print("Completed clicking.")
            clicking = False  # Reset clicking state after finishing
            x = 0  # Reset the click count if you want to restart the count
        else:
            pyautogui.leftClick()
            x += 1
        time.sleep(0.1)  # Optional: add a slight delay between clicks
    else:
        time.sleep(0.1)  # Prevent high CPU usage when not clicking

    # Check if the user presses Ctrl + Comma to toggle
    if keyboard.is_pressed('ctrl+comma'):
        toggle_clicking()
