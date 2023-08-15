from random import random


def to_grass_break():
    # 1.66 - 1.68
    return random() * 0.02 + 1.66


def use_cut_break():
    # 4 - 5 seconds
    return random() * 1 + 4


def seven_blocks():
    # 0.54 - 0.56 seconds
    return random() * 0.02 + 0.54


def eleven_blocks():
    # from 0.89 to 0.91 seconds
    return random() * 0.02 + 0.89


def three_blocks():
    # from 0.23 to 0.25 seconds
    return random() * 0.02 + 0.23


def leave_building():
    # 1.1 seconds to 1.2 seconds to leave building
    return random() * 0.1 + 1.1


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25


def heal_up_break():
    # dialogue of nurse healing break from 6 seconds to 7 seconds
    return random() * 1 + 6


# break from 0.1 - 0.25 seconds
def input_break():
    return random() * 0.15 + 0.1
