from time import *
import random as r



def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except Exception as e:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_r=round(time_delay,2)
    speed=len(userinput)/time_r
    return round(speed)

if __name__=='__main__':

    while True:
        ck=input(" Ready to test: yes/no:   ")
        if ck=="yes":
            test = ["The time module is a standard Python module that provides various functions for working with time-related operations. It offers functionalities for working with both system time and wall-clock time.",
            "my name is Remya","Welcome to Python Project"]
            test1=r.choice(test)
            print("*****    Typind speed calculator   *****")
            print(test1)
            print()
            print()

            time_1=time()
            testinput=input("Enter:     ")
            time_2=time()

            print()
            print('Speed:  ',speed_time(time_1,time_2,testinput),'w/sec')
            print('Error:   ',mistake(test1,testinput))
        elif ck=="no":
            print("Thank You!")
            break
        else:
            print("Wrong input")


