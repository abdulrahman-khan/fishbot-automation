# Fishbot Automation


## Running Discord Javascript 
1. Enable Developer Console
    open %appdata%/discord/settings.json
    change "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING": true

2. Open Developer Console

3. Paste fish2.js into developer console under the "Console" tab

## Python Captcha Script

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/fishbot-automation.git
    cd fishbot-automation
    ```

2. Install the required Python packages:
    ```sh
    pip install pygetwindow mss pillow pytesseract pywinauto pyautogui
    ```

3. Ensure Tesseract OCR is installed on your system. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

4. Open the Discord application and ensure it is visible on your screen.

5. Run the script:
    ```sh
    python captcha-verify.py
    ```
