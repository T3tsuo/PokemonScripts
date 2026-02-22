import time

import pyautogui
import pydirectinput

import random_breaks
from path_correction import self_align_side, self_align_up

backend_path = "scripts/PokemonScripts-main/ItemFarming/EverstoneFarming/"

outside_building = backend_path + "location/outside_building.png"

left_of_slide = backend_path + "location/left_of_slide.png"

under_slide = backend_path + "location/under_slide.png"

above_slide = backend_path + "location/above_slide.png"

battle_done = backend_path + "location/battle_done.png"


outside_building_align_val = 739
left_slide_align_val = 444
under_slide_align_val = 742
above_slide_align_val = 238


def wait_until_see(img, msg):
    while True:
        if pyautogui.locateOnScreen(img, confidence=0.8) is not None:
            # inside the house
            with open("log.txt", "a") as f_temp:
                print(msg, file=f_temp)
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    # while cannot find outside, keep on waiting
    wait_until_see(outside_building, "Left Building")


def go_into_cave():
    pydirectinput.press("1")
    with open("log.txt", "a") as f_temp:
        print("Bike", file=f_temp)
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.four_blocks())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    self_align_side(outside_building, outside_building_align_val)
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.thirty_two_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    self_align_up(left_of_slide, left_slide_align_val)
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.seven_blocks())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.input_break())
    self_align_side(under_slide, under_slide_align_val)
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.up_slide_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    self_align_up(above_slide, above_slide_align_val)
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.to_cave_break())
    pydirectinput.keyUp("right")
    wait_until_see(battle_done, "Inside of Cave")
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("right")
    pydirectinput.PAUSE = 0.1
    # break
    time.sleep(random_breaks.input_break())


def run():
    leave_building()
    go_into_cave()
