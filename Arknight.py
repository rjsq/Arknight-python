
import rpa as r
import concurrent.futures
import requests
import threading
import time
from system_hotkey import SystemHotkey
import sys

def automate_progress():
    hk = SystemHotkeys()
    hk.register(('control', '-'), callback=sys.exit())
    r.init(visual_automation = True, chrome_browser = False)
    try:
        while True:
            r.click('images/1.png')
            time.sleep(1)
          
            r.click('images/2.png')
            time.sleep(1)
         
            r.click('images/3.png')
            time.sleep(1)
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass


if __name__ == '__main__':
    automate_progress()