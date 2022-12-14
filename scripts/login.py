def register():
    # read the secret user file
    data = {}
    with open("../resources/database.txt", "r") as db:
        d, f = [], []
        for line in db:
            if len(line.strip()) > 0:
                a = line.split(",")
                if len(a) == 2:
                    d.append(a[0].strip())
                    f.append(a[1].strip())

        data = dict(zip(d, f))

    username = input("Create username: ")
    password = input("Create password: ")
    passwordconfirm = input("Re-enter password: ")

    if password != passwordconfirm:
        print("Password does not match, restart ")
        register()
    
    else:
        if len(password) < 1 and len(username) < 1:
            print("Username or Password too short, restart ")
            register()

        elif username in data:
            print("Username already exist, restart ")
            register()
        else :
            with open("database.txt", "a") as db:
                db.write(username + "," + password + "\n")
                print("Success! ")



def access():
    # read the secret user file
    data = {}
    with open("../resources/database.txt", "r") as db:
        d, f = [], []
        for line in db:
            if len(line.strip()) > 0:
                a = line.split(",")
                if len(a) == 2:
                    d.append(a[0].strip())
                    f.append(a[1].strip())

        data = dict(zip(d, f))

    while(True):
        # user prompt
        username = input("Enter username: ")
        password = input("Enter password: ")

        if len(username) < 1  or len(password) < 1:
            print("Both username & pwd should be at least 1 character long!")
            continue
        
        if  data.get(username):
            if  password == data.get(username):
                print("Login success ")
                break
            else:
                print("Username or password incorrect ")
                continue

        else:
            print("User not found ")
            register()
    

def home(option = None):
    option = input("Login | Signup: ")
    if option.lower() == "login":
        access()
    elif option.lower() == "signup":
        register()
    else:
        print("Please enter a valid option ")

home()