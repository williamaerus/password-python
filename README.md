# get started
this python script uses the sha256 method to check if the password is correct tho that you can't spot the right password from the file, don't use this file to secure your stuff because anyone could just open the file and delete the password checking form, this is just for you to have fun and play with this script.

 **SETUP**
 
 you can use [this](https://github.com/williamaerus/hash-with-python/blob/main/hash_text.py) other script that i wrote to hash your password, 
 
to setup your own password copy the sha256 of it and paste it at line 6 of the code `hashed_password = '' #this is the hash of the password` between the apostrophes

you may need to install the _hashlib_ library you can install it with this command `pip install hashlib`

**to add your own commands if the password is right**
you can add any command after line  between line 9 `#here you can add any command you want(remeber the indentation)` and line 12 `else:` (you can add lines of course, but don't change any code that was already written)

**to add your own commands if the password is wrong**
to do so delete line 20 of the script `close()` and add any command you want after it

now the script is setup and ready to go.

# how to use it
to start the script alone you have to run this command 

`python3 password.py` on linux

`python password.py` on windows

once the script is running it is gonna immediately ask for a password

if the password is correct then it is gonna print "correct password" and run any command you added
if the password is not correct then it is gonna ask to insert it again, you have 4 attempts to get the password right, after the script is gonna close by default or do something else if you personalized it.

**how to use the script in another file**

copy the password.py file in the directory of your script, then at the beginning of your script write 

`import password`

the script is gonna ask for the password by default everytime you start your script before doing anything else
# how does this work and why no one can discover the password from this script
as you know there is no way to reverse engineer a hash, so the script has the hash of the correct password stored in line 6.

to check if the password is correct it hashes the input (the password that your entered) and then check if the hash of the input is equal to the hash of the correct password, if it is correct it's gonna do whatever it's written in the code, if the password is incorrect it's gonna add one element to the list of wrong passwords and ask for the password again, once the list of wrong passwords contains 4 elements, the script is gonna kill himself by default or do whatever is written in the code.

every line of code is commented, so you can see what any line of code does
