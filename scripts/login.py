def read_user_data():
    # read the secret user file
    data = {}
    with open("resources/database.txt", "r") as db:
        d, f = [], []
        for line in db:
            if len(line.strip()) > 0:
                a = line.split(",")
                if len(a) == 2:
                    d.append(a[0].strip())
                    f.append(a[1].strip())

        data = dict(zip(d, f))

    return data


def register():
    # get user password details
    data = read_user_data()

    username = input("Create username: ")
    password = input("Create password: ")
    passwordconfirm = input("Re-enter password: ")

    if password != passwordconfirm:
        print("Password does not match, restart ")
        username = register()
        return username
    
    else:
        if len(password) < 1 and len(username) < 1:
            print("Username or Password too short!")
            username = register()
            return username

        elif username in data:
            print("Username already exists! Choose some other username")
            username = register()
            return username

        else :
            # write the new user to the user file
            with open("resources/database.txt", "a+") as db:
                db.write(username + "," + password + "\n")
                print("Success! ")
                return username



def access():
        # get user password details
    data = read_user_data()

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
                print("Incorrect Password")
                continue

        else:
            print("User not found ")
            username = register()
            break
    
    return username
    

def user_login():
    option = input("Login | Signup: ")
    if option.lower() == "login":
        username = access()
    else:
        username = register()

    return username

# user_login()