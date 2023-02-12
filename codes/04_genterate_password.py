import random
import string
import os

cahreters_for_pw = string.ascii_letters + string.digits + "!@#$%^&*()?"

def Generate_password(char,account_name,file_name="generated_passwords.txt",save="n",size=15):
    password = "".join(random.sample(char,size))
    print(password)
    if save == "y":
        with open(file_name,"a") as file:
            separator = "="*30
            file.write(f"\n{account_name}: \n{password}\n{separator}")
        print("passwoed saveed in: ",os.path.join(str(os.getcwd()),file_name))


size = input("Password Length (defualt=8): ")

if size == "":
    size = 8
else: 
    size = int(size)

account_name = input("input account name: ")
save = input("would you like to save it? (y)/n: ")

if save == "": 
    save = "y"
    file_name = input("file name for saved Passwords (defualt=generated_passwords.txt): ")
    if file_name == "":
        file_name = "generated_passwords.txt"
Generate_password(
    cahreters_for_pw,
    account_name=account_name,
    save=save,
    size=size,
    file_name=file_name)