from time import sleep
from random import random
import pickle
import sys
import os

import pyautogui
import pydirectinput

import random_breaks
from path_correction import self_align_side
from notify import check_mail_acc, ping_mail

backend_path = "scripts/PokemonScripts/BreedFarming/EeveeBreed/"

box_parent = backend_path + "images/breeding/box_parent.png"
ditto_parent = backend_path + "images/breeding/ditto_parent.png"
eevee_parent = backend_path + "images/breeding/eevee_parent.png"
breed_btn = backend_path + "images/breeding/breed_btn.png"
areyousure_dialog = backend_path + "images/breeding/areyousure_dialog.png"
yesorno = backend_path + "images/breeding/yesorno.png"
inside_house = backend_path + "images/location/inside_house.png"
cash_register = backend_path + "images/location/cash_register.png"

register_to_pc = 718

if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))


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


def breed():
    pydirectinput.keyDown("z")
    with open("log.txt", "a") as f_temp:
        print("Talking to Old Man", file=f_temp)
    wait_until_see(box_parent, "Select Box")
    pydirectinput.keyUp("z")
    sleep(random_breaks.input_break())
    mouse_click(box_parent)
    sleep(random_breaks.input_break())

    wait_until_see(ditto_parent, "Select Ditto")
    mouse_click(ditto_parent)
    sleep(random_breaks.input_break())

    wait_until_see(box_parent, "Select Box")
    mouse_click(box_parent)
    sleep(random_breaks.input_break())

    wait_until_see(eevee_parent, "Select Eevee")
    mouse_click(eevee_parent)
    sleep(random_breaks.input_break())

    wait_until_see(breed_btn, "BREED")
    mouse_click(breed_btn)
    sleep(random_breaks.input_break())

    wait_until_see(areyousure_dialog, "We are sure")
    pydirectinput.press("z")
    sleep(random_breaks.input_break())

    wait_until_see(yesorno, "Do not specify")
    pydirectinput.press("x")
    sleep(random_breaks.input_break())

    pydirectinput.keyDown("z")
    sleep(random_breaks.finish_convo())
    pydirectinput.keyUp("z")


def go_to_box():
    with open("log.txt", "a") as f_temp:
        print("Leaving Old Man", file=f_temp)
    # align with the house
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("left")
    sleep(random_breaks.input_break())
    pydirectinput.press("left")
    pydirectinput.PAUSE = 0.1
    sleep(random_breaks.input_break())
    # into the house
    pydirectinput.keyDown("up")
    sleep(random_breaks.into_house())
    pydirectinput.keyUp("up")
    sleep(random_breaks.input_break())
    wait_until_see(inside_house, "Inside House")
    # up to the lady
    pydirectinput.keyDown("up")
    sleep(random_breaks.to_lady())
    pydirectinput.keyUp("up")
    sleep(random_breaks.input_break())
    # align with pc box
    pydirectinput.keyDown("left")
    sleep(random_breaks.to_lady())
    pydirectinput.keyUp("left")
    sleep(random_breaks.input_break())
    self_align_side(cash_register, register_to_pc)
    # up to the pc box
    pydirectinput.keyDown("up")
    sleep(random_breaks.to_pc_box())
    pydirectinput.keyUp("up")
    sleep(random_breaks.input_break())


def run():
    breed()
    go_to_box()
