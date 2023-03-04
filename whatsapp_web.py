from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def whatsappMsg(name, message):

    startfile("https://web.whatsapp.com/") 

    sleep(15)

    click(x=166, y=258)

    sleep(1)

    write(name)    

    sleep(2)

    click(x=313, y=441)

    sleep(2)

    write(message)

    press('enter')


def whatsappcall(name):
    
    startfile("C:\\Users\\shrekar reddy\\Downloads\\WhatsAppSetup.exe") 

    sleep(20)

    click(x=98, y=135)

    sleep(1)

    write(name)    

    sleep(2)

    click(x=317, y=304)

    sleep(2)

    click(x=1742, y=80)


def whatsappchat(name):
    
    startfile("https://web.whatsapp.com/") 

    sleep(20)

    click(x=98, y=135)

    sleep(1)

    write(name)    

    sleep(2)

    click(x=317, y=304)

