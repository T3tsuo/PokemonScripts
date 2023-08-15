import breed_return
import ditto_return
from time import sleep
import pydirectinput
import os
import pickle

# this program breeds a eevee's with dittos and repeats until box 10 is fully empty

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

if os.path.isfile("email.dat"):
    google_email = pickle.load(open("email.dat", "rb"))

if os.path.isfile("mail_password.dat"):
    mail_password = pickle.load(open("mail_password.dat", "rb"))

if os.path.isfile("log.txt"):
    os.remove("log.txt")
with open('log.txt', 'w') as f:
    pass


def run():
    with open("log.txt", "a") as f_temp:
        print("Starting Script", file=f_temp)
    sleep(2)
    pydirectinput.press("x")
    with open("log.txt", "a") as f_temp:
        print("Toggle Run", file=f_temp)
    while True:
        breed_return.run()
        ditto_return.run()
