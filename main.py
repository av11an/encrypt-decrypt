import pyAesCrypt
import os

def deCrypt():
    encryptedMessage = input("What is the filename? (ex. name) no extensions:\n")
    password = input("Password for file?:\n")
    try:
        pyAesCrypt.decryptFile(encryptedMessage+".txt.aes", encryptedMessage+"Decrypted.txt", password)
        print("Message decrypted! Output in -> " + encryptedMessage+"Decrypted.txt")
    except:
        print("Wrong password!")
        deCrypt()

def enCrypt(password, messageToSend):
    with open("placeholder.txt", "w") as f1:
        f1.write(messageToSend)
    fileName = input("Encrypted file name:\n")
    pyAesCrypt.encryptFile("placeholder.txt", fileName+".txt.aes", password)
    os.remove('placeholder.txt')

def getMessNPass():
    messageToSend = input("What Message would you like to share?:\n")
    password = input("What password do would you like to use to secure that message?:\n")
    passwordVF = input("Put that password in one more time to verify you wrote it correctly:\n")
    if (password == passwordVF):
        enCrypt(password, messageToSend)
        print("\nYour message has been encrypted thank you!")
    else:
        goBack = input("Password did not match try again?(y) or Go back?(n)\n")
        if (goBack == "y"):
            getMessNPass()
        elif (goBack == "n"):
            main()
        else:
            print("Bad Choice!")
            main()


def main():
    enOrDeQ = input("Do you want to encrypt(e) or decrypt(d) a message?\n")
    if (enOrDeQ == "e"):
        print("Encrypt")
        getMessNPass()
    elif(enOrDeQ == "d"):
        print("Decrypt")
        deCrypt()
    else:
        print("bad choice!")
        main()


if __name__ == '__main__':
    main()

