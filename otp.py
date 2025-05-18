#!/usr/bin/env python3
import pyotp
import qrcode
import time
import qrcode.image.svg
from sys import argv



with open("key.txt", 'r') as infile:
    secret = infile.readline().rstrip("\n")

name = "Raulp"
issuer = "BigTech"
totp = pyotp.TOTP(s=secret, name=name, issuer=issuer)


def no_params():
    current_otp = totp.at(time.time())
    print(totp.interval)
    print("Current OTP is: ", current_otp)
    print("-" * 10)
    print ("Syncronizing local timer with Google")
    print("Please be patient...")
    
    while current_otp == totp.now():
        pass

    print("Syncronization complete")
    print("A valid OTP will be printed every 30 seconds.")
    print(totp.interval)
    while True:
    
        print(totp.now())
        for i in range(30):
            print(".", end='', flush=True)
            time.sleep(1)
        print()    


def generate_qr():

    uri = totp.provisioning_uri(name, issuer)
    my_qr = qrcode.make(uri, image_factory=qrcode.image.svg.SvgFillImage)
    filename = 'otp-qr.svg'
    my_qr.save(filename)
    print("Saving QR code in file: ",filename )


def get_otp():
    print(f"one time password: ", totp.now())



if __name__ == "__main__":

    try:
        if len(argv) == 1:
            no_params()
        if len(argv) == 2:
            if argv[1] == "--get-otp":
                get_otp()
            elif argv[1] == "--generate-qr":
                generate_qr()
            else:
                print("Error: command not recognized.")
                exit()
        else:
            print("Error: Too many arugments")
            
    except KeyboardInterrupt:
        print("\nexiting...")
        exit()

