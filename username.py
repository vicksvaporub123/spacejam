from random import *
def entry_check(str1,li):
        if str1 in li:
            print("The username you entered already exists")
            print("Try these usernames:")
            x=1
            while x<4:
                temp=str1 + str(randint(1,1000))
                if temp not in li:
                    print(temp)
                    x+=1
                else:
                    continue
        else:
            if len(str1)<8:
                print("Your username must be at least 8 characters long")
                print("Try these usernames:")
                x=1
                while x<4:
                    temp=str1+str(randint(10**(8-len(str1)),10**(10-len(str1))))
                    if temp not in li:
                        print(temp)
                        x+=1
                    else:
                        continue
            else:
                li.append(str1)
while True:
    list_user=['vicksvaporub123','Linx','Ujwal','Vishakha']
    print("Enter choice:")
    ch=int(input("1 for manual username entry, 2 for username generator, 3 for password generator and 0 for exit:"))
    if ch==0:
        break
    elif ch==1:
        s=input("Enter username:")
        entry_check(s,list_user)
    elif ch==2:
        randlist=['']