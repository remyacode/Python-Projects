def add(a,b):
    ans=a+b
    print('---------------')
    print("|  "+str(a)+" + "+str(b)+" = "+str(ans)+"  |")
    print('---------------')
def sub(a,b):
    ans=a-b
    print('---------------')    
    print("|  "+str(a)+" - "+str(b)+" = "+str(ans)+"  |")
    print('---------------')
def mul(a,b):
    ans=a*b
    print('---------------')
    print("|  "+str(a)+" x "+str(b)+" = "+str(ans)+"  |")
    print('---------------')

def div(a,b):
    ans=a/b
    print('---------------')
    print("|  "+str(a)+" / "+str(b)+" = "+str(ans)+"  |")
    print('---------------')

while True:
    print('Choose your operation')
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice=input("Enter your choice:    ")
    choice=choice.upper()

    if choice=='E':
        print('Exit')
        quit()
    a=int(input('a: '))
    b=int(input('b: '))
    if choice=='A':

        print('Addition')
        add(a,b)
    if choice=='B':
        print('Subtraction')
        sub(a,b)
    if choice=='C':
        print('Multiplication')
        mul(a,b)
    if choice=='D':
        print('Division')
        div(a,b)

