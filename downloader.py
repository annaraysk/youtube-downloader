#! python3

from selenium import webdriver
import pyperclip 
import time
import pyautogui as au
from selenium.webdriver.common.keys import Keys
print("\nWelcome to Python Youtube downloader\n\n")
print("copy the youtube link to your clipboard\npress 'y' if it is already copied\n")
i = input()

if (i=='y' or i == 'Y'):
    print("your youtube link is   "+pyperclip.paste())
    
    c = webdriver.Chrome()
    c.get("https://saveitoffline.com/#"+pyperclip.paste())
    bu1=c.find_element_by_css_selector("#expandFormats > span")
    bu1.click()
    time.sleep(2)
    bu = c.find_element_by_css_selector("#additionalFormats > a:nth-child(17) > div")
    bu.click()
    time.sleep(2)
    print("\n\ndownloading audio...\n\n\n")
s=input()
