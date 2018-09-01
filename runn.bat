@echo off
pip install selenium
pip install pyperclip
pip install pyautogui
pip install chromedriver

py c:\downloader.py %*
pause