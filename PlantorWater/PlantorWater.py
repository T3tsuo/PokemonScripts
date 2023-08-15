import time
import os
import pickle

import abundant_shrine
import mistralton
from shiny_notify import check_mail_acc, ping_mail

if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))

if os.path.isfile("log.txt"):
    os.remove("log.txt")
with open('log.txt', 'w') as f:
    pass


def run(place, action):
    global google_email, mail_password
    # time for user to switch windows
    with open("log.txt", "a") as f_temp:
        print("Starting Script", file=f_temp)
    time.sleep(2)
    if place == "Mistralton":
        mistralton.do_all(action)
    elif place == "Abundant Shrine":
        abundant_shrine.do_all(action)

    if check_mail_acc():
        ping_mail(google_email, mail_password, "Script is DONE")
