import sys
import time
import pickle
import os
from random import random
import pyautogui
import pydirectinput
from shiny_notify import ping_mail, check_mail_acc

import random_breaks

battle_done = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/battle_done.png"

battle_done_2 = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/battle_done_2.png"

at_left_cave = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/at_left_cave.png"

at_right_cave = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/at_right_cave.png"

fight_option = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/in_battle_options/fight_option.png"

run_option = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/in_battle_options/run_option.png"

ditto_png = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/ditto.png"

shiny_png = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/shiny_pokemon.png"

horde_png = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/horde.png"

payday_move = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/pokemon_moves/payday_move.png"

falseswipe_move = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/pokemon_moves/falseswipe_move.png"

assist_move = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/pokemon_moves/assist_move.png"

one_pp = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/in_battle_options/one_pp.png"

inside_tunnel_2 = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/inside_tunnel_2.png"

inside_house = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/inside_house.png"

outside_house = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/outside_house.png"

pokemon_summary = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/pokemon_summary.png"

inside_building = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/location/inside_building.png"

bag_option = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/in_battle_options/bag_option.png"

balls_option = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/in_battle_options/balls_option.png"

red_health = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/in_battle_options/red_health.png"

yellow_health = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/in_battle_options/yellow_health.png"

duskball_png = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/balls/duskball.png"

duskball_highlighted_png = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/balls/duskball_highlighted.png"

asleep_png = "scripts/PokemonScripts/PokemonFarming/DittoFarm/images/balls/asleep.png"

right_left_move = "right"

ball_count = 0

if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))


def wait_until_see(img, msg):
    while True:
        if pyautogui.locateOnScreen(img, confidence=0.8) is not None:
            # inside the house
            with open("log.txt", "a") as f_temp:
                print(msg, file=f_temp)
            break
        else:
            time.sleep(0.1)


def search_wild_pokemon():
    global right_left_move
    with open("log.txt", "a") as f_temp:
        print("Searching for Pokemon", file=f_temp)
    pydirectinput.keyDown(right_left_move)
    time.sleep(random_breaks.input_break())
    while True:
        if pyautogui.locateOnScreen(at_left_cave, confidence=0.8) is not None and right_left_move == "left":
            pydirectinput.keyUp(right_left_move)
            time.sleep(random_breaks.input_break())
            right_left_move = "right"
            pydirectinput.keyDown(right_left_move)
            with open("log.txt", "a") as f_temp:
                print("Right", file=f_temp)
        elif pyautogui.locateOnScreen(at_right_cave, confidence=0.8) is not None and right_left_move == "right":
            pydirectinput.keyUp(right_left_move)
            time.sleep(random_breaks.input_break())
            right_left_move = "left"
            pydirectinput.keyDown(right_left_move)
            with open("log.txt", "a") as f_temp:
                print("Left", file=f_temp)
        if pyautogui.locateOnScreen(battle_done, confidence=0.8) is None and \
                pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is None:
            pydirectinput.keyUp(right_left_move)
            with open("log.txt", "a") as f_temp:
                print("In Battle", file=f_temp)
            time.sleep(random_breaks.input_break())
            return


def is_health_low():
    if pyautogui.locateOnScreen(red_health, grayscale=False) is not None or \
            pyautogui.locateOnScreen(yellow_health, grayscale=False) is not None:
        with open("log.txt", "a") as f_temp:
            print("Low Health", file=f_temp)
        return True
    return False


def in_battle():
    global google_email, mail_password
    # wait until battle
    while True:
        if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
            break
        else:
            time.sleep(0.1)
    # check first if it's a shiny, then ditto, then horde, then others
    if pyautogui.locateOnScreen(shiny_png, confidence=0.8) is not None:
        with open("log.txt", "a") as f_temp:
            print("Shiny Pokemon", file=f_temp)
        if check_mail_acc():
            ping_mail(google_email, mail_password, "SHINY FOUND")
        sys.exit(0)
    elif pyautogui.locateOnScreen(ditto_png, confidence=0.8) is not None:
        with open("log.txt", "a") as f_temp:
            print("Ditto", file=f_temp)
        return catch_ditto()
    elif pyautogui.locateOnScreen(horde_png) is not None:
        with open("log.txt", "a") as f_temp:
            print("Horde", file=f_temp)
        run_away()
        return False
    else:
        with open("log.txt", "a") as f_temp:
            print("Others", file=f_temp)
        return payday()


def catch_ditto():
    is_one_pp = False
    # click fight
    location = pyautogui.locateOnScreen(fight_option, confidence=0.8)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
    pydirectinput.click()
    with open("log.txt", "a") as f_temp:
        print("Fight", file=f_temp)
    time.sleep(random_breaks.paying_attention_break())
    # run away if we have no pp
    if pyautogui.locateOnScreen(one_pp, confidence=0.8) is not None:
        with open("log.txt", "a") as f_temp:
            print("Final PP", file=f_temp)
        is_one_pp = True
    # or else try to catch
    location = pyautogui.locateOnScreen(falseswipe_move, confidence=0.8)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
    pydirectinput.click()
    with open("log.txt", "a") as f_temp:
        print("False Swipe", file=f_temp)
    # wait and then use assist
    wait_until_see(fight_option, "Time to fight")
    time.sleep(random_breaks.input_break())
    # check health
    health = is_health_low()
    while True:
        # if pokemon is asleep
        if pyautogui.locateOnScreen(asleep_png) is not None:
            throw_ball(duskball_png, duskball_highlighted_png)
            time.sleep(random_breaks.input_break())
        # if not then put it to sleep
        else:
            # click fight
            location = pyautogui.locateOnScreen(fight_option, confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)
            pydirectinput.click()
            with open("log.txt", "a") as f_temp:
                print("Fight", file=f_temp)
            # check if we are on last pp
            if pyautogui.locateOnScreen(one_pp, confidence=0.8) is not None:
                with open("log.txt", "a") as f_temp:
                    print("Final PP", file=f_temp)
                is_one_pp = True
            # use assist
            location = pyautogui.locateOnScreen(assist_move, confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)
            pydirectinput.click()
            with open("log.txt", "a") as f_temp:
                print("Assist", file=f_temp)
            wait_until_see(fight_option, "Time to Fight")
            time.sleep(random_breaks.input_break())
            health = is_health_low()
        if is_one_pp is False:
            while True:
                if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
                    # battle is not done
                    time.sleep(random_breaks.input_break())
                    health = is_health_low()
                    break
                elif pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None or \
                        pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is not None:
                    # battle is done
                    time.sleep(random_breaks.input_break())
                    # if pokemon summary pops up then hit back
                    if pyautogui.locateOnScreen(pokemon_summary) is not None:
                        pydirectinput.press("x")
                        time.sleep(random_breaks.input_break())
                    return health
                else:
                    time.sleep(0.1)
        else:
            while True:
                if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
                    # no more pp, then just throw ball
                    throw_ball(duskball_png, duskball_highlighted_png)
                    time.sleep(random_breaks.input_break())
                elif pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None or \
                        pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is not None:
                    # battle is done
                    time.sleep(random_breaks.input_break())
                    # if pokemon summary pops up then hit back
                    if pyautogui.locateOnScreen(pokemon_summary) is not None:
                        pydirectinput.press("x")
                        time.sleep(random_breaks.input_break())
                    return True
                else:
                    time.sleep(0.1)


def throw_ball(img1, img2):
    global ball_count, google_email, mail_password
    # click bag
    location = pyautogui.locateOnScreen(bag_option, confidence=0.8)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
    pydirectinput.click()
    with open("log.txt", "a") as f_temp:
        print("Bag", file=f_temp)
    while True:
        if pyautogui.locateOnScreen(balls_option) is None:
            # go to pokeballs
            pydirectinput.press("right")
            time.sleep(random_breaks.input_break())
        else:
            # at the pokeballs
            break
    # throw pokeball
    location = pyautogui.locateOnScreen(img1)
    if location is None:
        location = pyautogui.locateOnScreen(img2)
    pyautogui.moveTo(location.left + random() * location.width,
                     location.top + random() * location.height)
    pydirectinput.click()
    time.sleep(random_breaks.input_break())
    pydirectinput.click()
    with open("log.txt", "a") as f_temp:
        print("Throwing DuskBall", file=f_temp)
    ball_count -= 1
    with open("log.txt", "a") as f_temp:
        print(str(ball_count) + " balls left", file=f_temp)
    # no more balls so quit
    if ball_count == 0:
        if check_mail_acc():
            ping_mail(google_email, mail_password, "No more balls")
        sys.exit(0)


def payday():
    is_one_pp = False
    while True:
        # click fight
        location = pyautogui.locateOnScreen(fight_option,
                                            confidence=0.8)
        pyautogui.moveTo(location.left + random() * location.width,
                         location.top + random() * location.height)
        pydirectinput.click()
        with open("log.txt", "a") as f_temp:
            print("Fight", file=f_temp)
        time.sleep(random_breaks.paying_attention_break())
        # run away if we have no pp
        if pyautogui.locateOnScreen(one_pp, confidence=0.8) is not None:
            with open("log.txt", "a") as f_temp:
                print("Final PP", file=f_temp)
            is_one_pp = True
        # or else use payday
        location = pyautogui.locateOnScreen(payday_move, confidence=0.8)
        pyautogui.moveTo(location.left + random() * location.width,
                         location.top + random() * location.height)
        pydirectinput.click()
        with open("log.txt", "a") as f_temp:
            print("Pay Day", file=f_temp)
        # check if battle is done or if we need to keep on fighting
        if is_one_pp is False:
            while True:
                if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
                    # battle is not done
                    time.sleep(random_breaks.input_break())
                    break
                elif pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None or \
                        pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is not None:
                    # battle is done
                    time.sleep(random_breaks.input_break())
                    return False
                else:
                    time.sleep(0.1)
        else:
            # no more pp
            while True:
                if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
                    # battle is not done
                    run_away()
                    return True
                elif pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None or \
                        pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is not None:
                    # battle is done
                    time.sleep(random_breaks.input_break())
                    return True
                else:
                    time.sleep(0.1)


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
        elif pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None or \
                pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is not None:
            # ran away successfully
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)


def go_heal_up():
    # use dig
    pydirectinput.press("6")
    with open("log.txt", "a") as f_temp:
        print("Dig", file=f_temp)
    time.sleep(random_breaks.input_break())
    wait_until_see(inside_tunnel_2, "Inside Tunnel")
    time.sleep(random_breaks.input_break())
    # leave tunnel
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.three_blocks_break())
    pydirectinput.keyUp("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("right")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.person_tunnel_break() + 0.1)
    pydirectinput.keyUp("down")
    wait_until_see(inside_house, "Inside House")
    time.sleep(random_breaks.input_break())
    # leave house
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.into_tunnel_break() + 0.1)
    pydirectinput.keyUp("down")
    wait_until_see(outside_house, "Outside House")
    time.sleep(random_breaks.input_break())
    # teleport
    pydirectinput.press("5")
    with open("log.txt", "a") as f_temp:
        print("Teleport", file=f_temp)
    wait_until_see(inside_building, "Inside Building")
    time.sleep(random_breaks.input_break())
    # heal up
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.heal_up_break())
    pydirectinput.keyUp("z")
    with open("log.txt", "a") as f_temp:
        print("Healing Done", file=f_temp)
    time.sleep(random_breaks.input_break())


def lineup_in_cave():
    # go up by two
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    time.sleep(3)
    # check to see if we're in a battle
    while True:
        if pyautogui.locateOnScreen(battle_done, confidence=0.8) is None:
            in_battle()
            # ran away successfully
            time.sleep(random_breaks.input_break())
        else:
            break
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())


def run(x):
    global ball_count
    ball_count = x
    # go up in cave while checking if encountered pokemon
    lineup_in_cave()
    heal_up = False
    while heal_up is False:
        search_wild_pokemon()
        heal_up = in_battle()
    go_heal_up()
    return ball_count
