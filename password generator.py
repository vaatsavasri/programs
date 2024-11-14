import random
import string
length=int(input("enter length of password"))
print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')
while(True):
    choice=int(input("pick a number"))
    characterlist=""
    if(choice==1):
        characterlist +=string.ascii_letters
    elif(choice==2):
        characterlist +=string.digits
    elif(choice==3):
        characterlist +=string.punctuation
    elif(choice==4):
        break
    else:
        print("pick a valid option")
        
password=[]
for i in range(length):
    randomchar=random.choice(characterlist)
    password.append(randomchar)
    print("the random password is" + "".join(password))
    
