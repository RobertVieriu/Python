import pyautogui
import time
import keyboard


def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\Capture_URL_final.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\Capture_URL_final.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://www.youtube.com')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_search():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\Capture_Search.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\Capture_Search.png', confidence=0.7)
        pyautogui.click(camp_google)
        pyautogui.write('loltyler1')
        pyautogui.press('enter')
        time.sleep(3)
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\Capture_Channel.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        keyboard.press('k')
        keyboard.release('k')
    else:
        print("Imaginea nu este pe ecran")


def cautare_subscribe():
    time.sleep(1)
    
    camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\Capture_Subscribe.png', confidence=0.7)
    pyautogui.click(camp_google)
    time.sleep(1)

def cautare_video():
    time.sleep(1)

    if pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\videos.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\videos.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")

    time.sleep(1)
    if pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\tyler1.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\tyler1.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")
    time.sleep(1)
  

def coordonate():
    print(pyautogui.position())

col=1

while not keyboard.is_pressed('esc'):
    coordonate()

def lol():
    keyboard.press('win')
    keyboard.release('win')
    time.sleep(1)
    pyautogui.write('league of legends')
    pyautogui.press('enter')
    time.sleep(18)
    if pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\play_button.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\play_button.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\ranked.png', confidence=0.7)
        pyautogui.click(camp_google)
        camp_google = pyautogui.locateOnScreen(r'D:\Proiecte\Python_Projects\confirm.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Imaginea nu este pe ecran")
  

cautare_google()
cautare_search()
cautare_subscribe()
cautare_video()
lol()