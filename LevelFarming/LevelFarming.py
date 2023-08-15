import os
import time
import pydirectinput

import fight
import heal_return

# this program xp levels pokemon

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

if os.path.isfile("log.txt"):
    os.remove("log.txt")
with open('log.txt', 'w') as f:
    pass


def run(x=None):
    if x is None:
        # then ask for amount of times user can use sweet scent before going to pokecenter
        x = input("Number of times to use sweet scent: ")
    x = int(x)
    with open("log.txt", "a") as f_temp:
        print("Starting Script", file=f_temp)
    time.sleep(2)
    pydirectinput.press("x")
    with open("log.txt", "a") as f_temp:
        print("Toggle Run", file=f_temp)
    # loop forever
    while True:
        heal_return.run()
        fight.run(x)

