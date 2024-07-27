from random import random


def to_cave_break():
    # 2.97 - 2.99
    return random() * 0.02 + 2.97


def up_slide_break():
    # 1.18 - 1.2
    return random() * 0.02 + 1.18


def seven_blocks():
    # 0.55 - 0.57
    return random() * 0.02 + 0.55


def thirty_two_blocks():
    # 2.63 - 2.65
    return random() * 0.02 + 2.63


def four_blocks():
    # 0.3 - 0.32
    return random() * 0.02 + 0.3


def leave_building():
    # 1.8 seconds to 1.9 seconds to leave building
    return random() * 0.1 + 1.8


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25


def heal_up_break():
    # dialogue of nurse healing break from 9 seconds to 14 seconds
    return random() * 5 + 9


def input_break():
    # break from 0.1 - 0.25 seconds
    return random() * 0.15 + 0.1
