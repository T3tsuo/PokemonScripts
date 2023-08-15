import pydirectinput
import time

import random_breaks


def water():
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.water_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())
    with open("log.txt", "a") as f_temp:
        print("Watered", file=f_temp)


def plant():
    # select which seeds
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())
    # plant them
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())
    with open("log.txt", "a") as f_temp:
        print("Planted", file=f_temp)


def first_plant():
    # get to the section where you have to pick your seeds
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
    # wait for user to manually enter the seeds and go through the dialogue
    time.sleep(15)
    with open("log.txt", "a") as f_temp:
        print("Planted", file=f_temp)
    time.sleep(2)
