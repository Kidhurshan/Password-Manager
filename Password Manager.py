from cryptography.fernet import Fernet

# ask to add password, view password
# for add
    # get the username and password
    # write into the file
#for view
    # get the text from file line by line
    # seperate the username and password
    # print it in the terminal

#for the encryption and decryption is used by Fernet package
# using the documentation to do the encryption and decryption
# the important section is to encode() , decode() method for string

'''def add_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)'''

def view_key():
    with open("key.key","rb") as file:
        key = file.read()
        return key

print("Welcome to Password Manager :)")
key = view_key()
ferent = Fernet(key)

def add():
    userName = input("Enter the user name: ")
    password = input("Enter the password: ")

    with open("password.txt","a") as file:
        file.write(f"{userName}|{ferent.encrypt(password.encode()).decode()}\n")       #here we password -> byte format -> encrypt it -> back to string(decode() method)

def view():
    with open("password.txt","r") as file:
        for line in file.readlines():
            line = line.rstrip()
            user, password = line.split("|")
            print(f"User name : {user}  &   Password : {ferent.decrypt(password.encode()).decode()}")       #here we password -> byte format -> decrypt it -> back to string
                                                        # encode for string -> byte , decode for byte -> string
                                                        # if we not using this byte string will appear ex: b'stringWord'

while(True):
    userChoice = input ("VIEW Password? or ADD new Password? (view/add): ").lower()
    if userChoice == "view":
        view()
    elif userChoice == "add":
        add()
    elif userChoice == "q":
        break
    else:
        print("Invalid answer, Try again")