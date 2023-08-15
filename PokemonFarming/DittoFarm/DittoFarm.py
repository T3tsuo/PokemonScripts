import time
import os

import catch_ditto
import heal_return

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

if os.path.isfile("log.txt"):
    os.remove("log.txt")
with open('log.txt', 'w') as f:
    pass


def run(ball_num=None):
    if ball_num is None:
        ball_num = input("How many dusk balls do you have (number): ")
    ball_num = int(ball_num)
    if ball_num > 1:
        with open("log.txt", "a") as f_temp:
            print("Starting with " + str(ball_num) + " balls", file=f_temp)
    elif ball_num == 1:
        with open("log.txt", "a") as f_temp:
            print("Starting with " + str(ball_num) + " ball", file=f_temp)
    time.sleep(2)
    # loop forever
    while True:
        heal_return.run()
        ball_num = catch_ditto.run(ball_num)
