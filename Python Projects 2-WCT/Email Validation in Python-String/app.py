email=input('Enter Email:   ') # g@g.in - minimum
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-3]=='.') ^ (email[-4]=='.'): #XOR
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print('Wrong Email 5 (Space, Uppercase)')
                else:
                    print('Correct')
                
            else:
                print('Wrong Email 4 ( . position error)')
        else:
            print('Wrong Email 3 (@ error)')
    else:
        print('Wrong Email 2 (First Letter Error)')
else:
    print('Wrong Email 1 (minimum length error)')
