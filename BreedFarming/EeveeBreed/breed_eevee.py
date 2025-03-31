from time import sleep
from random import random
import pickle
import sys
import os

import pyautogui
import pydirectinput

import random_breaks
from notify import check_mail_acc, ping_mail

backend_path = "scripts/PokemonScripts/BreedFarming/EeveeBreed/"

box_parent = backend_path + "images/breeding/box_parent.png"
pc_deposit_box = backend_path + "images/box/pc_deposit_box.png"
box_5 = backend_path + "images/box/box_5.png"
ditto_box = backend_path + "images/box/ditto_box.png"
eevee_box = backend_path + "images/box/eevee_box.png"
breed_slot_1 = backend_path + "images/box/breed_slot_1.png"
breed_slot_2 = backend_path + "images/box/breed_slot_2.png"
eevee_hatched = backend_path + "images/breeding/eevee_hatched.png"
breed_btn = backend_path + "images/breeding/breed_btn.png"
areyousure_dialog = backend_path + "images/breeding/areyousure_dialog.png"


if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))


def mouse_click(img, right=False):
    location = pyautogui.locateOnScreen(img, confidence=0.8, grayscale=False)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
    if right:
        pydirectinput.rightClick()
    else:
        pydirectinput.click()


def wait_until_see(img, msg):
    counter = 0
    while True:
        if pyautogui.locateOnScreen(img, confidence=0.8, grayscale=False) is not None:
            # inside the house
            with open("log.txt", "a") as f_temp:
                print(msg, file=f_temp)
            break
        else:
            counter += 1
            sleep(0.1)

        # wait 15 minutes before time out
        if counter >= 900:
            with open("log.txt", "a") as f_temp:
                print("Timed Out", file=f_temp)
            if check_mail_acc():
                ping_mail(google_email, mail_password, "Timed Out")
            sys.exit(0)


def breed():
    wait_until_see(eevee_hatched, "Start Breeding")
    pydirectinput.keyDown("z")
    with open("log.txt", "a") as f_temp:
        print("Talking to Old Man", file=f_temp)
    wait_until_see(box_parent, "Select Box")
    pydirectinput.keyUp("z")
    sleep(random_breaks.input_break())
    mouse_click(box_parent)
    sleep(random_breaks.input_break())
    wait_until_see(box_5, "Select Box 5")
    sleep(random_breaks.input_break())
    mouse_click(box_5)
    sleep(random_breaks.input_break())
    wait_until_see(ditto_box, "Select Ditto")
    sleep(random_breaks.input_break())
    mouse_click(ditto_box, right=True)
    sleep(random_breaks.input_break())

    wait_until_see(breed_slot_1, "Select Slot")
    sleep(random_breaks.input_break())
    mouse_click(breed_slot_1)
    sleep(random_breaks.input_break())

    # move mouse away in case
    wait_until_see(pc_deposit_box, "Move Mouse")
    sleep(random_breaks.input_break())
    mouse_click(pc_deposit_box)
    sleep(random_breaks.input_break())

    wait_until_see(eevee_box, "Select Eevee")
    mouse_click(eevee_box)
    sleep(random_breaks.input_break())

    wait_until_see(breed_slot_2, "Select Slot")
    sleep(random_breaks.input_break())
    mouse_click(breed_slot_2)
    sleep(random_breaks.input_break())

    wait_until_see(breed_btn, "BREED")
    mouse_click(breed_btn)
    sleep(random_breaks.input_break())

    wait_until_see(areyousure_dialog, "We are sure")
    pydirectinput.press("z")
    sleep(random_breaks.input_break())

    pydirectinput.keyDown("z")
    sleep(random_breaks.finish_convo())
    pydirectinput.keyUp("z")


def run():
    breed()
