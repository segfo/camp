import hashlib
import getpass
import rpisec

f=open("password.txt","w")
f.write(hashlib.sha512(getpass.getpass()+rpisec.SALT).hexdigest())
f.close()
print("password updated.")
