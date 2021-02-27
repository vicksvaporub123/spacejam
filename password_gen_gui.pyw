import tkinter
import string
import pyperclip
import random

######################################################################################################################################################################
#initializing basic window
root = tkinter.Tk()
root.geometry('300x250')
root.resizable(0,0)
root.title('Password and Username Generator')
titl = tkinter.Label(text = 'Password Generator', font = ('Arial',25)).grid()


######################################################################################################################################################################
#necessary variables and moficication function
constraints = {'upper':False, 'integer':False, 'special':False}
passw = ''
pwd = tkinter.StringVar()



#the three functions below are used to toggle the constraints for userselection of password format
def uppertoggle():
    global constraints
    if constraints['upper']==False:
        constraints['upper']=True
    elif constraints['upper']==True:
        constraints['upper']=False

def inttoggle():
    global constraints
    if constraints['integer']==False:
        constraints['integer']=True
    elif constraints['integer']==True:
        constraints['integer']=False

def specialtoggle():
    global constraints
    if constraints['special']==False:
        constraints['special']=True
    elif constraints['special']==True:
        constraints['special']=False



#the password generator function
def passGen(length,c):
    import random
    import string
    global passw
    global pwd
    passw = ''
    for i in range(length):
        a = random.randint(0,3)
        if a==0 and c['upper']==True:
            passw+=random.choice(string.ascii_uppercase)
        elif a==1 and c['integer']==True:
            passw+=random.choice(string.digits)
        elif a==3 and c['special']==True:
            passw+=random.choice(string.punctuation)
        else:
            passw+=random.choice(string.ascii_lowercase)
    pwd.set(passw)
    print(passw,pwd)




#defined function to copy password generated
def copy_pass(passw):
    import pyperclip
    pyperclip.copy(passw)


######################################################################################################################################################################

### SETUP FOR OBTAINING PASSWORD LENGTH
lentext = tkinter.Label(text = 'Password Length').grid()
pass_len = tkinter.IntVar()
lent = tkinter.Spinbox(root, from_=8, to_=16, textvariable = pass_len, width = 4).grid()



### SETUP FOR PASSWORD FORMAT
uppers =  tkinter.Checkbutton(root, text = 'Include Uppercase', command = uppertoggle).grid()
integers = tkinter.Checkbutton(root, text = 'Include Integers', command = inttoggle).grid()
special = tkinter.Checkbutton(root, text = "Include Special Characters", command = specialtoggle).grid()



#GENERATING BUTTON 
genbut = tkinter.Button(root, text = 'Generate New Password', command = lambda:passGen(pass_len.get(),constraints)).grid()
tkinter.Entry(root,textvariable = pwd).grid()



copybut = tkinter.Button(root, text = 'Copy Password', command=lambda:copy_pass(passw)).grid()

root.mainloop()

