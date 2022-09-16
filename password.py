import hashlib
attempts = [] # a list of all the wrong attempts
def start():
    pswd = input('password: ')
    hashed_string = hashlib.sha256(pswd.encode('utf-8')).hexdigest() #creates a hash of the input (pswd)
    hashed_password = '' #this is the hash of the password
    if hashed_string == hashed_password: #if the hash of the input is equal to the hash of the password then print correct password
        print("correct password")
        #here you can add any command you want(remeber the indentation)


    else:
        attempts.append(pswd) #appends every wrong password to the wrong passwords list
        nmbs = len(attempts) #measures how long the wrong password list is
        if nmbs <= 3: #if the list is shorter or equal at 3 then ask the password again
            print('incorrect password try again')
            print(4 - nmbs,'attempts left')
            start()
        elif nmbs > 3: #if the list is longer then 3 then exit
            #to personalize delete exit() and add any command you want (remeber the indentation)
            exit()
start()
