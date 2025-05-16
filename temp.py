import pyotp
import pyotp.utils
import qrcode
import base64

secret = "POTATOES2porque3"
name = "RaulP"
issuer = "BigTech"


totp = pyotp.TOTP(secret, name=name, issuer=issuer)
my_uri = totp.provisioning_uri(name, issuer)
print(my_uri)

my_qr = qrcode.make(my_uri)


my_qr.save('temp.png')



