from random import random


def go_to_grass_break():
    # 3.8 - 3.81 seconds
    return random() * 0.01 + 3.8


def leave_building():
    # 1.8 seconds to 1.9 seconds to leave building
    return random() * 0.1 + 1.8


def input_break():
    # break for hoping on bike from 0.1 - 0.25 seconds
    return random() * 0.15 + 0.1


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25


def heal_up_break():
    # dialogue of nurse healing break from 9 seconds to 12 seconds
    return random() * 3 + 9
