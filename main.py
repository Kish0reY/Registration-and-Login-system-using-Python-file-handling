import re


# pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$'
# user = '^[a-zA-Z][\._]?[0-9]?+[@][a-z]+[.][a-z]{2,3}$'

# Registration

def register():
    # database
    db = open('database.txt', 'r')
    d = []
    f = []
    for i in db:
        u, p = i.split(",")
        p = p.strip()
        d.append(u)
        f.append(p)

    # Email ID
    email = input("Create Email ID:")

    pattern = '^[a-zA-Z]+[.\_]?[0-9]+[@][a-z]+[.][a-z]{2,3}$'
    if re.search(pattern, email):
        print('Valid Email ID')
    else:
        print('Invalid Email ID')
    register()

    # password
    pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$'
    password = input("Create password:")
    result = re.findall(pattern, password)
    password1 = input("Confirm password:")

    if result != password1:
        print("Passwords don't match, restart")
        register()

    elif len(password) < 5 or len(password) > 16:
        print("Password too short or exceeding limit. restart:")
        register()
    elif email in d:
        print('Email ID exists')
        register()
    else:
        db = open("database.txt", "a")
        db.write(email + ", " + password + "\n")
        print("Success!")
    access()


# Login
def access():
    db = open('database.txt', 'r')
    email = input("Enter Email ID:")
    password = input("Enter password:")
    if not len(email or password) < 1:
        d = []
        f = []
        for i in db:
            u, p = i.split(',')
            p = p.strip()
            d.append(u)
            f.append(p)
        data = dict(zip(d, f))
        print(data)

        try:
            if email == data[d]:
                print('Email ID exist')
            else:
                try:
                    if password == f:
                        print('Login success')
                        print('welcome')
                    else:
                        print('incorrect Email ID or Password')

                except:
                    print('incorrect Email ID or Password')

        except:
            print('Login error')

    else:
        print('Try again')


# Password Reset
def new():
    db = open('database.txt', 'a')
    email = input("Enter Email ID:")
    s = []
    while s:
        s = db.readline()
        d = s.split(',')
        if d[0] == email:
            password = input("Create New password:")
            pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$'
            result = re.findall(pattern, password)
            password1 = input("Confirm New password:")

            if result != password1:
                print("Passwords don't match, restart")
                new()

            elif len(password) < 5 or len(password) > 16:
                print("Password too short or exceeding limit. restart:")
                new()
        else:
            db.write(email+", "+password+ "\n")
            print("Success!")
    db.close()

# Homepage

def home():
    print('choose an option')
    option = input('Login | Register | Reset Password:')
    if option == 'Login':
        access()
    elif option == 'Register':
        register()
    elif option == 'Reset Password':
        new()
    else:
        print('Enter valid option')

    return


home()
