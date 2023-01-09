from cryptography.fernet import Fernet

'''

# key + password + text to encyprt = random text
# random text + key + password = text to encrypt

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()  # turns string into bytes
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # rstrip is gonna delete the line break we did
            data = line.rstrip()
            # will split anything once they see that character
            user, pssw = data.split("/")
            # example: "hello/tim/2" will split into ['hello', 'tim', '2']
            # when putting like that in comas, first element will be "user" and second "pssw"
            print("User: ", user, "/ Password: ",
                  fer.decrypt(pssw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    # we are creating a file that doesn't exist
    # with open closes the file after, which is similar to:
    # file = open ('passwords.txt, 'a'):
    # file.close()
    # modes:
    # w(write, clear and overwrite an existant file)
    # r(read, only reads the file)
    # a(appends, create a new file)
    with open('passwords.txt', 'a') as f:
        # the \n is the line break
        f.write(name + " / " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add)? Press q to quit. ".lower())
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
