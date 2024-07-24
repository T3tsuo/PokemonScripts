from time import sleep
from random import random
import pickle
import sys
import os

import pyautogui
import pydirectinput

import random_breaks
from notify import check_mail_acc, ping_mail
from path_correction import self_align_side

backend_path = "scripts/PokemonScripts/BreedFarming/EeveeBreed/"

box_10 = backend_path + "images/box/box_10.png"
ditto_box = backend_path + "images/box/ditto_box.png"
wall_sign = backend_path + "images/location/wall_sign.png"
outside_building = backend_path + "images/location/outside_building.png"
eevee_hatched = backend_path + "images/breeding/eevee_hatched.png"

if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))

sign_to_door = 723


def mouse_click(img):
    location = pyautogui.locateOnScreen(img, confidence=0.8, grayscale=False)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
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


def get_ditto():
    # goes to box 10
    pydirectinput.keyDown("z")
    wait_until_see(box_10, "Select Box 10")
    pydirectinput.keyUp("z")
    mouse_click(box_10)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
    pydirectinput.click()
    sleep(random_breaks.input_break())

    wait_until_see(ditto_box, "Grab Ditto")
    pydirectinput.keyDown("ctrlleft")
    mouse_click(ditto_box)
    pydirectinput.keyUp("ctrlleft")
    sleep(random_breaks.input_break())

    pydirectinput.press("x")
    sleep(random_breaks.input_break())
    pydirectinput.press("x")
    sleep(random_breaks.input_break())
    with open("log.txt", "a") as f_temp:
        print("Exit PC Box", file=f_temp)


def back_to_breed():
    # to the table
    pydirectinput.keyDown("down")
    sleep(random_breaks.to_lady())
    pydirectinput.keyUp("down")
    sleep(random_breaks.input_break())
    # align with door
    pydirectinput.keyDown("right")
    sleep(random_breaks.to_entrance())
    pydirectinput.keyUp("right")
    sleep(random_breaks.input_break())
    self_align_side(wall_sign, sign_to_door)
    pydirectinput.keyDown("down")
    sleep(random_breaks.into_house())
    pydirectinput.keyUp("down")
    sleep(random_breaks.input_break())
    wait_until_see(outside_building, "Outside")

    pydirectinput.PAUSE = 0.03
    pydirectinput.press("down")
    sleep(random_breaks.input_break())
    pydirectinput.press("down")
    sleep(random_breaks.input_break())
    pydirectinput.press("right")
    sleep(random_breaks.input_break())
    pydirectinput.press("right")
    sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.1
    wait_until_see(eevee_hatched, "Start Breeding")


def run():
    get_ditto()
    back_to_breed()
