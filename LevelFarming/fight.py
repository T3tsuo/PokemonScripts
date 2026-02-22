import time
import sys
import os
import pickle
from random import random
import pydirectinput
import pyautogui

import random_breaks
from shiny_notify import ping_mail, check_mail_acc

backend_path = "scripts/PokemonScripts-main/LevelFarming/"

battle_done = backend_path + "location/battle_done.png"

inside_building = backend_path + "location/inside_building.png"

rapidash_png = backend_path + "location/rapidash.png"

run_option = backend_path + "location/run_option.png"

fight_option = backend_path + "location/fight_option.png"

surf_option = backend_path + "location/surf_option.png"

earthquake_option = backend_path + "location/earthquake_option.png"

shiny_png = backend_path + "location/shiny_pokemon.png"

if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))


def heal_up():
    at_nurse = False
    # we are not at nurse yet
    while at_nurse is False:
        # once we are at the nurse
        if pyautogui.locateOnScreen(inside_building, confidence=0.8) is not None:
            # then set flag to true, so we can talk to the nurse
            at_nurse = True
            with open("log.txt", "a") as f_temp:
                print("At Nurse", file=f_temp)
            time.sleep(0.5)
        else:
            time.sleep(0.5)

    # talk through dialogue
    with open("log.txt", "a") as f_temp:
        print("Talking to Nurse", file=f_temp)
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.heal_up_break())
    pydirectinput.keyUp("z")
    with open("log.txt", "a") as f_temp:
        print("Healing Done", file=f_temp)
    # break
    time.sleep(random_breaks.input_break())


def teleport_away():
    # press teleport
    pydirectinput.press('5')
    with open("log.txt", "a") as f_temp:
        print("Teleport", file=f_temp)
    time.sleep(random_breaks.paying_attention_break())


def which_to_attack():
    with open("log.txt", "a") as f_temp:
        print("SELECT #2", file=f_temp)
    # select the second pokemon
    pydirectinput.press("z")
    time.sleep(random_breaks.paying_attention_break())


def kill_all():
    # in battle
    while True:
        # fight
        while True:
            if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
                location = pyautogui.locateOnScreen(fight_option,
                                                    confidence=0.8)
                pyautogui.moveTo(location.left + random() * location.width,
                                 location.top + random() * location.height)
                # click fight
                pydirectinput.click()
                with open("log.txt", "a") as f_temp:
                    print("Fight", file=f_temp)
                time.sleep(random_breaks.input_break())
                break
        # surf or earthquake
        while True:
            if pyautogui.locateOnScreen(surf_option, confidence=0.8) is not None:
                location = pyautogui.locateOnScreen(surf_option,
                                                    confidence=0.8)
                pyautogui.moveTo(location.left + random() * location.width,
                                 location.top + random() * location.height)
                # click surf
                pydirectinput.click()
                with open("log.txt", "a") as f_temp:
                    print("Surf", file=f_temp)
                time.sleep(random_breaks.input_break())
                break
            elif pyautogui.locateOnScreen(earthquake_option, confidence=0.8) is not None:
                location = pyautogui.locateOnScreen(earthquake_option,
                                                    confidence=0.8)
                pyautogui.moveTo(location.left + random() * location.width,
                                 location.top + random() * location.height)
                # click earthquake
                pydirectinput.click()
                with open("log.txt", "a") as f_temp:
                    print("Earthquake", file=f_temp)
                time.sleep(random_breaks.input_break())
                break
        # select and attack the second pokemon
        which_to_attack()
        # check if battle is done or fight option is back up
        while True:
            if pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None:
                with open("log.txt", "a") as f_temp:
                    print("Battle Done", file=f_temp)
                time.sleep(random_breaks.input_break())
                return
            elif pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
                # continue fighting
                time.sleep(random_breaks.input_break())
                break


def run_away():
    while True:
        if pyautogui.locateOnScreen(run_option, confidence=0.8) is not None:
            location = pyautogui.locateOnScreen(run_option,
                                                confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)
            pydirectinput.click()
            with open("log.txt", "a") as f_temp:
                print("Run Away", file=f_temp)
        elif pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None:
            # ran away successfully
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)


def in_battle():
    global google_email, mail_password
    while True:
        if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
            # in battle
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)
    # check shiny
    if pyautogui.locateOnScreen(shiny_png, confidence=0.8) is not None:
        if check_mail_acc():
            ping_mail(google_email, mail_password, "SHINY FOUND")
        sys.exit(0)
    # if not shiny then fight
    elif pyautogui.locateOnScreen(rapidash_png, confidence=0.8) is not None:
        time.sleep(random_breaks.input_break())
        with open("log.txt", "a") as f_temp:
            print("Fight Rapidash", file=f_temp)
        return kill_all()
    else:
        time.sleep(random_breaks.input_break())
        return run_away()


def run(x):
    for i in range(x):
        # use sweet scent
        pydirectinput.press('4')
        with open("log.txt", "a") as f_temp:
            print("Sweet Scent", file=f_temp)
        # use fight them to gain xp
        in_battle()
    # when all of sweet scent is used then leave to pokecenter
    teleport_away()
    # then heal up
    heal_up()
