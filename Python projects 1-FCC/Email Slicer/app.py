print("")
print("EMAIL SLICER")
print("")
email=input('Enter Email Id: ')

(username,domain)=email.split('@')
(domain,ext)=domain.split('.')

print('Username:    ',username)
print('Domain:  ',domain)
print('Extension:   ',ext)


