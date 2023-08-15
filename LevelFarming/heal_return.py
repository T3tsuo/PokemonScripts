import time
import pydirectinput
import pyautogui

import random_breaks

outside_building = "scripts/LevelFarming/location/outside_building.png"


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    # while cannot find outside, keep on waiting
    is_outside = False
    while is_outside is False:
        # if image recognition detects that we left the building
        if pyautogui.locateOnScreen(outside_building, confidence=0.8) is not None:
            # then we are outside
            is_outside = True
            with open("log.txt", "a") as f_temp:
                print("Left Building", file=f_temp)
            time.sleep(0.5)
        else:
            time.sleep(0.5)


def go_to_grass():
    # hop on bike
    pydirectinput.press("1")
    with open("log.txt", "a") as f_temp:
        print("Bicycle", file=f_temp)
    time.sleep(random_breaks.input_break())
    # go left
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.go_to_grass_break())
    pydirectinput.keyUp("left")
    with open("log.txt", "a") as f_temp:
        print("At Grass", file=f_temp)
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    # break
    time.sleep(random_breaks.input_break())


def run():
    leave_building()
    go_to_grass()
