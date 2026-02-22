import time

import pyautogui
import pydirectinput

import random_breaks
from path_correction import self_align_side
from path_correction import self_align_vertical

backend_path = "scripts/PokemonScripts-main/ItemFarming/AmuletFarming/"

outside_building = backend_path + "location/outside_building.png"

sign_fence = backend_path + "location/sign_fence.png"

table = backend_path + "location/table.png"

bills_machine = backend_path + "location/bills_machine.png"


outside_building_align_val = 0
sign_fence_align_val = 0

table_align_val = 437
bills_machine_align_val = 830


def wait_until_see(img, msg):
    while True:
        if pyautogui.locateOnScreen(img, confidence=0.8) is not None:
            # we are there
            with open("log.txt", "a") as f_temp:
                print(msg, file=f_temp)
            break
        else:
            time.sleep(0.1)


def leave_building():
    # go down
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building_down())
    pydirectinput.keyUp("down")
    # check if aligned
    self_align_vertical(table, table_align_val)
    # go right
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.leave_building_right())
    pydirectinput.keyUp("right")
    # check if aligned
    self_align_side(bills_machine, bills_machine_align_val)
    # go down
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    # while cannot find outside, keep on waiting
    wait_until_see(outside_building, "Left Building")
    time.sleep(random_breaks.input_break())


def go_to_grass():
    # hop on bike
    pydirectinput.press("1")
    with open("log.txt", "a") as f_temp:
        print("Bicycle", file=f_temp)
    time.sleep(random_breaks.input_break())
    # go left
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.three_blocks())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    # check if aligned
    self_align_side(outside_building, outside_building_align_val)
    # go down
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.eleven_blocks())
    pydirectinput.keyUp("down")
    time.sleep(random_breaks.input_break())
    # go right
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.seven_blocks())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.input_break())
    # check if aligned
    self_align_side(sign_fence, sign_fence_align_val)
    # look down
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
    # use cut
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.use_cut_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.input_break())
    # go to grass
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.to_grass_break())
    pydirectinput.keyUp("down")
    with open("log.txt", "a") as f_temp:
        print("At Grass", file=f_temp)
    time.sleep(random_breaks.paying_attention_break())


def run():
    leave_building()
    go_to_grass()
