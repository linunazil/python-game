def register():
    db = open("database.txt", "r")
    Username = input("Create username: ")
    Password = input("Create password: ")
    Passwordconfirm = input("Re-enter password: ")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))


    if Password != Passwordconfirm:
        print("Password does not match, restart ")
        register()
    else:
        if len(Password) < 6:
            print("Password too short, restart ")
            register()


        elif Username in d:
            print("Username already exist, restart ")
            register()
        else :
            db = open("database.txt", "a")
            db.write(Username + ", " + Password + "\n")
            print("Success! ")



def access():
    db = open("database.txt", "r")
    Username = input("Enter username: ")
    Password = input("Password password: ")

    if not len(Username or Password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if  data[Username]:
                try:
                    if  Password == data[Username]:
                        print("Login success ")
                    else:
                        print("Username or password incorrect ")
                        home()
                except:
                    print("Incorrect Username or password ")
                    home()
            else:
                print("User not found ")
                home()
        except:
            print("Error")
            home()
    else:
        print("Please enter a value ")
        home()

def home(option = None):
    option = input("Login | Signup: ")
    if option.lower() == "login":
        access()
    elif option.lower() == "signup":
        register()
    else:
        print("Please enter a valid option ")
home()