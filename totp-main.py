import pyotp
import time
import datetime
time.timezone
from sys import argv


with open("key.txt", 'r') as infile:
    secret = infile.readline().rstrip("\n")
totp = pyotp.TOTP(s=secret, name="RaulP", issuer="BigTech")


def no_params():
    current_otp = totp.at(time.time())
    print("Current TOTP is: ", current_otp)
    print("-" * 10)
    print ("Syncronizing local timer with google's")
    print("Please be patient...")
    while current_otp == totp.now():
        pass
    print("Syncronization complete")
    print("A valid OTP will be printed every 30 seconds.")
    while True:
        print(totp.now())
        for i in range(30):
            print(".", end='', flush=True)
            time.sleep(1)
        print()    


def get_otp():
    print(f"one time password: ", totp.now())


if __name__ == "__main__":

    if len(argv) > 1:
        if argv[1] == "--get-otp":
            get_otp()
        else:
            print("Error: did not recognize argument")
    else:
        no_params()
            
