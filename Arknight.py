
import rpa as r
import time

def automate_progress():
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
