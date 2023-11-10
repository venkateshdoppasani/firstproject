import pyautogui as spam
import time

limit=input("no.of messages")
msg=input("message you want to send")

i=0

time.sleep(5)

while i<int(limit):
    spam.typewrite(msg)
    spam.press('enter')

    i+=1

edited
