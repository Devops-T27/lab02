print("Login")
email = input("email please: ")
password = input("password: ")

def login(email,password):
     f = open("users.txt","r", encoding="utf-8")
     for ligne in f:
        list=ligne.split()
        eml=list[1]
        pas=list[2]
        if eml == email and pas == password:
            return True
    f.close()
    return False
        

if login(email,password):
    print("you logged in")
else:
    print("your email or password is incorrect")
