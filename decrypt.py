#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet # pyright: ignore[reportMissingImports]
files=[]
for file in os.listdir():
    if file == "voldermort.py" or file=="thekey.key" or file=="decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
with open("thekey.key",'rb') as key:
    secretkey=key.read()
secretphrase="Hello!"
user_phrase= input("Enter the secret phrase to decrypt your files:\n")
if user_phrase==secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents=thefile.read()
        contents_decrypted= Fernet(secretkey).decrypt(contents)
        with open(file,'wb') as thefile:
            thefile.write(contents_decrypted)
    #print(key)
    print(files)
    print("Files decrypted")
else:
    print("Incorrect secret phrase!!")