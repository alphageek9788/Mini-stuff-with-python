import pyautogui

def screenshot():
    # Take screenshot
    pic = pyautogui.screenshot()

    # Save the image
    pic.save('Screenshot.png')

screenshot()