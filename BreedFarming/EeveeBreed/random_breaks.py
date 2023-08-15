from random import random


def input_break():
    # break from 0.1 - 0.25 seconds
    return random() * 0.15 + 0.1


def into_house():
    # break from 0.6 - 0.62 seconds
    return random() * 0.02 + 0.6


def to_pc_box():
    # break from 0.5 - 0.52 seconds
    return random() * 0.02 + 0.5


def to_lady():
    # break from 0.9 - 0.92 seconds
    return random() * 0.02 + 0.9


def to_entrance():
    # break from 0.8 - 0.82 seconds
    return random() * 0.02 + 0.8


def finish_convo():
    # break from 8 - 9 seconds
    return random() * 1 + 8


def to_table():
    # break from 0.5 - 0.52 seconds
    return random() * 0.02 + 0.5
