print("Login")
email = input("email please: ")
password = input("password: ")

def login(email,password):
    f = open("users.txt","r")
    for ligne in f:
        user = ligne.split()
        if user[1]==email and user[2]==password:
            return True
    f.close()
    return False
        

if login(email,password):
    print("you logged in")
else:
    print("your email or password is incorrect")