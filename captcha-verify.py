import time
import pygetwindow as gw
import mss
from PIL import Image
import pytesseract
import re
import pywinauto
import pyautogui
""" captures a screenshot of discord window, OCR to extract text,
    finds captcha verification code, sends the verification code as keystrokes to the discord window."""

# Function to capture a screenshot of a specified window
def capture_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        bbox = {
            'top': window.top,
            'left': window.left,
            'width': window.width,
            'height': window.height
        }
        with mss.mss() as sct:
            img = sct.grab(bbox)
            img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            return img
    except IndexError:
        print(f"Window titled '{window_title}' not found.")
        return None

# find verification code
def find_verification_code():
    pattern1 = r"Please use /verify (\w+) to continue playing."
    pattern2 = r"(?<=\n)[a-zA-Z0-9]{3,6}(?=\n)"
    with open("output.txt", 'r', encoding='utf-8', errors='ignore') as file:
        contents = file.read()
    
    # Search for the verification code using regex
    match = re.search(pattern1, contents)
    if match:
        return match.group(1)
    else:
        match = re.search(pattern2,contents)
        return match.group(0) if match else None
    
def main():
    while(True):
        window_title = ""
        # Get all window titles and find the title of the discord window
        windows = gw.getAllTitles()
        for title in windows:
            if 'discord' in title.lower(): 
                window_title = title
                break
        if not window_title:
            print("Discord Not found - Please open the window")
            return
        app = pywinauto.Application().connect(title=window_title)
        app.window(title=window_title).set_focus()

        # screenshot        
        img = capture_window(window_title)
        if img:
            img.save("screenshot.png")
            # Extract text from the screenshot using OCR
            text = pytesseract.image_to_string(img)
            with open("output.txt", "w") as text_file: 
                text_file.write(text)

        verification_code = find_verification_code()
        if verification_code:
            print(f"Verification code found: {verification_code}")
            if text:
                # Type the verification code and press enter
                pyautogui.write("/verify " + verification_code, interval=0.05)
                pyautogui.press('enter')
                # Exit the program after sending the verification code
                exit()
        
        # screenshot every 2 seconds
        time.sleep(2)

if __name__ == "__main__":
    main()
