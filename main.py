import time
import random
import pyautogui as pg
from playsound import playsound                  # `If you dont want to playsound just backspace this line`


# `///======================================================================Buffer Time=====================================================================================///`
time.sleep(5)


# `///====================================================================Global Variables==================================================================================///`


c_wrk = ["pls hl", "pls search", "pls hl"]

works = ["pls fish", "pls hunt", "pls dig", "pls beg"]

ping_cmnds = ["pls gift 1 kno @Abid", "pls give all @Abid"]

item_dict = {'ant': 1, 'apple': 1, 'boar': 1, 'candy': 1, 'coin': 1,
             'common': 1, 'cookie': 1, 'deer': 1, 'duck': 1, 'exotic': 1,
             'fresh': 1, 'garbage': 1, 'hol': 1, 'junk': 1, 'ladybug': 1,
             'landmine': 1, 'laptop': 1, 'pizza': 1, 'rabbit': 1, 'rarefish': 1,
             'sand': 1, 'sea': 1, 'shovel': 1, 'stickbug': 1, 'worm': 1
             }


# `///======================================================================Global Functions================================================================================///`


# _ping requests need two enter commands_


def ping():
    for _ in range(2):
        pg.press("enter")


# For gifting every item in inventory from dummy account
 # `Pls gift no longer works with Dank Memer Update 9.10.5`

def gift_all(dct):
    for item, quantity in dct.items():
        pg.typewrite(f'pls gift {quantity} {item} @Dummy_Account')
        ping()
        time.sleep(random.randint(18,24))


# Only 1/3 chance of catching
# click() -> This is too hopefully catch collectable items if they appear in mini-game


def click():
    pg.click(x=580, y=650)
    time.sleep(random.randint(2,4))


# gamble_search() -> To click the higher, lower, jackpot buttons and other 'pls search' item buttons


def gamble_search(x):
    for i in range(3):
        pg.typewrite(x[i])
        pg.press("enter")
        time.sleep(random.randint(1,3))
        click()
        time.sleep(random.randint(12,15))


# `///======================================================================Program Start Point==============================================================================///`


for j in range(2):
    if j == 1: 
        playsound("ringtone.mp3") # => Alarm for you too check if you died. Feel free to disable if you want

    for work in works:
        pg.typewrite(work)
        pg.press("enter")
        time.sleep(3)
        pg.click(x=480, y=675)
        time.sleep(random.randint(1,3))

    for ping in ping_cmnds:
        pg.typewrite(ping)
        ping()
        time.sleep(random.randint(1,3))

    gamble_search(c_wrk)

gift_all(item_dict)
