import pyautogui as p
import time as t
clik = p.locateOnScreen('coccoc.png')
p.doubleClick(clik)
t.sleep(1)
p.write('facebook.com',interval=0.15)
p.press('enter')
t.sleep(10)
cik = p.locateOnScreen('post.png')
p.click(cik)
t.sleep(1)
p.write('xin chao K62 va K63',interval=0.15)
t.sleep(1)
# p.hotkey('ctrl','enter')
cliksend = p.locateOnScreen('send.png')
p.doubleClick(click)  