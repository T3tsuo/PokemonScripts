import time
import pyautogui
import pydirectinput

import random_breaks
from path_correction import self_align_side

backend_path = "scripts/PokemonScripts-main/PokemonFarming/DittoFarm/"

outside_building = backend_path + "images/location/outside_building.png"

inside_house = backend_path + "images/location/inside_house.png"

inside_tunnel = backend_path + "images/location/inside_tunnel.png"

battle_done = backend_path + "images/location/battle_done.png"

battle_done_2 = backend_path + "images/location/battle_done_2.png"

align_door = backend_path + "images/location/align_door.png"

run_option = backend_path + "images/in_battle_options/run_option.png"

fishermen_to_door = 362


def wait_until_see(img, msg):
    while True:
        if pyautogui.locateOnScreen(img, confidence=0.8) is not None:
            # inside the house
            with open("log.txt", "a") as f_temp:
                print(msg, file=f_temp)
            break
        else:
            time.sleep(0.1)


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    # while cannot find outside, keep on waiting
    wait_until_see(outside_building, "Left Building")
    time.sleep(random_breaks.input_break())


def go_to_house():
    # hop on bike
    pydirectinput.press("1")
    with open("log.txt", "a") as f_temp:
        print("Bicycle", file=f_temp)
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.into_sign_break())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    # go down
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("down")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.align_house_break())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    # check and fix if aligned to the house by comparing to fishermen
    self_align_side(align_door, fishermen_to_door)
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.four_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    wait_until_see(inside_house, "Inside House")
    time.sleep(random_breaks.input_break())


def go_into_tunnel():
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.into_tunnel_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    wait_until_see(inside_tunnel, "Inside Tunnel")
    time.sleep(random_breaks.input_break())


def go_into_cave():
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.person_tunnel_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("left")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.three_blocks_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("right")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    wait_until_see(battle_done, "Inside Cave")
    time.sleep(random_breaks.input_break())
    # hop on bike
    pydirectinput.press("1")
    with open("log.txt", "a") as f_temp:
        print("Bicycle", file=f_temp)
    time.sleep(random_breaks.input_break())


def run():
    leave_building()
    go_to_house()
    go_into_tunnel()
    go_into_cave()
