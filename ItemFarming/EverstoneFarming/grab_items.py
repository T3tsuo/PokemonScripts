import time
import os
import sys
import pickle
import pyautogui
import pydirectinput
from random import random

import random_breaks
from heal_return import wait_until_see
from shiny_notify import ping_mail, check_mail_acc
from battle_log_config import two_log_region

stole_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/battle_logs/stole.png"

flinched_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/battle_logs/flinched.png"

banette_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/banette.png"

mount_coronet_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/mount_coronet_entrance.png"

frisked_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/battle_logs/frisked_geodude.png"

everstone_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/take_everstone.png"

hard_stone_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/take_hard_stone.png"

inside_building = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/inside_building.png"

battle_done = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/battle_done.png"

fight_option = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/fight_option.png"

run_option = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/run_option.png"

thief_move = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/thief_move.png"

shiny_png = "scripts/PokemonScripts/ItemFarming/EverstoneFarming/location/shiny_pokemon.png"

if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))


def heal_up():
    wait_until_see(inside_building, "At Nurse")
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


def thief():
    # counter to keep track of which pokemon is currently selected
    select_pokemon = 0
    # while the item is not found, and we still have not attacked all 5 pokemons
    while select_pokemon < 3:
        # click fight
        location = pyautogui.locateOnScreen(fight_option,
                                            confidence=0.8)
        pyautogui.moveTo(location.left + random() * location.width,
                         location.top + random() * location.height)
        pydirectinput.click()
        time.sleep(random_breaks.paying_attention_break())
        # click thief
        location = pyautogui.locateOnScreen(thief_move,
                                            confidence=0.8)
        pyautogui.moveTo(location.left + random() * location.width,
                         location.top + random() * location.height)
        pydirectinput.click()
        with open("log.txt", "a") as f_temp:
            print("Thief", file=f_temp)
        time.sleep(random_breaks.paying_attention_break())
        # select and attack specific pokemon
        which_to_attack(select_pokemon)
        # stole item
        stole_item = False
        # if pokemon flinches
        flinched = False
        # wait for entire attack break while checking if thief took an item
        turn_done = False
        while turn_done is False:
            # if turn is done
            if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
                turn_done = True
            # if item is found
            if pyautogui.locateOnScreen(stole_png, confidence=0.8, region=two_log_region()) is not None \
                    and stole_item is False:
                with open("log.txt", "a") as f_temp:
                    print("Stole Item", file=f_temp)
                stole_item = True
            if pyautogui.locateOnScreen(flinched_png, confidence=0.8, region=two_log_region()) is not None:
                flinched = True
                with open("log.txt", "a") as f_temp:
                    print("Flinched", file=f_temp)
            if pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None:
                with open("log.txt", "a") as f_temp:
                    print("Horde is dead", file=f_temp)
                # if item was stolen
                if pyautogui.locateOnScreen(stole_png, confidence=0.8) is not None:
                    with open("log.txt", "a") as f_temp:
                        print("Stole Item", file=f_temp)
                    return True
                else:
                    # return that item was not found
                    return False
        time.sleep(random_breaks.input_break())
        if stole_item:
            # return that item was found
            return True
        if not flinched:
            select_pokemon += 1
    return False


def which_to_attack(n):
    with open("log.txt", "a") as f_temp:
        print("SELECT #" + str(n + 1), file=f_temp)
    if n == 0:
        # select the second pokemon
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())
    elif n == 1:
        # go down to select the third pokemon
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        # select it
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())
    elif n == 2:
        # go down to select the fourth pokemon
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        # select it
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())


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


def teleport_away():
    # use dig
    pydirectinput.press("6")
    with open("log.txt", "a") as f_temp:
        print("Dig", file=f_temp)
    time.sleep(random_breaks.paying_attention_break())
    wait_until_see(mount_coronet_png, "Outside")
    # press teleport
    pydirectinput.press('5')
    with open("log.txt", "a") as f_temp:
        print("Teleport", file=f_temp)
    time.sleep(random_breaks.paying_attention_break())


def in_battle():
    global google_email, mail_password
    # keep on checking until we are in battle
    wait_until_see(fight_option, "Time to Fight")
    # check shiny
    if pyautogui.locateOnScreen(shiny_png, confidence=0.8) is not None:
        if check_mail_acc():
            ping_mail(google_email, mail_password, "SHINY FOUND")
        sys.exit(0)
    # once we can fight, check if we found item
    elif pyautogui.locateOnScreen(frisked_png, region=two_log_region()) is not None:
        with open("log.txt", "a") as f_temp:
            print("Found Item", file=f_temp)
        # switch to attacking stage
        took_item = thief()
        # switch to run away the pokemons if battle isn't done
        if pyautogui.locateOnScreen(battle_done, confidence=0.8) is None:
            run_away()
        with open("log.txt", "a") as f_temp:
            print("Battle End", file=f_temp)
        # found item but return if we took the item
        return True, took_item
    # did not find any items on pokemon so did not take it
    return False, False


def action_take(item_img, msg):
    location = pyautogui.locateOnScreen(item_img,
                                        confidence=0.8)
    with open("log.txt", "a") as f_temp:
        print(msg, file=f_temp)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
    pydirectinput.click()
    time.sleep(random_breaks.paying_attention_break())
    return True


def take_item():
    item_taken = False
    while item_taken is False:
        if pyautogui.locateOnScreen(banette_png, confidence=0.8) is not None:
            # grab location of image
            location = pyautogui.locateOnScreen(banette_png, confidence=0.8)
            # click randomly on the box
            pyautogui.moveTo(location.left + random() * location.width, location.top + random() * location.height)
            pydirectinput.click()
            with open("log.txt", "a") as f_temp:
                print("Banette Selected", file=f_temp)
            # user paying attention reaction time
            time.sleep(random_breaks.paying_attention_break())
            while item_taken is False:
                # check which item was taken and proceed to remove it from the pokemon
                if pyautogui.locateOnScreen(everstone_png, confidence=0.8):
                    item_taken = action_take(everstone_png, "Taking Everstone")
                elif pyautogui.locateOnScreen(hard_stone_png, confidence=0.8):
                    item_taken = action_take(hard_stone_png, "Taking Hard Stone")


def run(x):
    for i in range(x):
        # use sweet scent
        pydirectinput.press('4')
        with open("log.txt", "a") as f_temp:
            print("Sweet Scent", file=f_temp)
        # check if item was found and if it was it will try to get it and return if it did or didn't
        found_item, took_item = in_battle()
        if not found_item and not took_item:
            with open("log.txt", "a") as f_temp:
                print("Not Found", file=f_temp)
            # run away if battle isn't done
            if pyautogui.locateOnScreen(battle_done, confidence=0.8) is None:
                # run away from battle
                run_away()
        elif found_item and took_item:
            # if item is stolen then take it off of your pokemon
            take_item()
    # when all of sweet scent is used then leave to pokecenter
    teleport_away()
    # then heal up
    heal_up()
