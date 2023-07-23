import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")

def genpass():
    password_length=int(input("Length:  "))
    random.shuffle(characters)
    password=[]

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password="".join(password)

    print(password)

option=input("Do you want a password? (yes/no): ")
if option=='yes':
    genpass()
elif option=='no':
    print("Thank You")
    quit()
else:
    print("Invalid Input")
    quit()