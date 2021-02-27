import tkinter
import string
import pyperclip
import random

######################################################################################################################################################################
#initializing basic window
root = tkinter.Tk()
root.geometry('300x550')
root.resizable(0,0)
root.title('PwD & UserName Generator')
titl = tkinter.Label(text = 'Password Generator', font = ('Arial',25)).grid()


######################################################################################################################################################################
######################################################################################################################################################################
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
tkinter.Label(root,).grid() 
genbut = tkinter.Button(root, text = 'Generate New Password', command = lambda:passGen(pass_len.get(),constraints),bg='light green',fg='black',font=('unispace',8,'bold')).grid()
tkinter.Label(root,).grid()
tkinter.Entry(root,textvariable = pwd).grid()
tkinter.Label(root,).grid()

copybut = tkinter.Button(root, text = 'Copy Password', command=lambda:copy_pass(passw),bg = 'light blue',fg='black',font=('unispace',8,'bold')).grid()

######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################


#creating necessary list and variables
l1=['Lando','Inga','Grim','Charitable','Tau','A9ent','Zed','Doped','Prince','Sheriff','Hateful','Loco','Salty','Khaleesi','Duke','Drax','Illusory','Overdramatic','Odona','Major','Damned','Queen','Doctor']
l2=['Bok','Odis','Shanker','Golem','Organa','Obscen3','Baltar','Butch','Monolith','Boss','Expert','Betty','Samurai','Ace','Sting','Cognus','Winds','Temptress','Vindictus','Flasher','Tidecaller','Cheese','Kid']
usern = ''
user = tkinter.StringVar()



#easy sounding username generator function
def usergen1():
    import random
    import string
    global usern
    global user
    usern=''
    global l1,l2
    x=random.choice(l1)
    y=random.choice(l2)
    z=random.randint(10,1000)
    usern=x+y+str(z)
    user.set(usern)


#defined function to copy username generated
def copy_user(usern):
    import pyperclip
    pyperclip.copy(usern)


######################################################################################################################################################################

#labels for spacings
tkinter.Label(root,text = '-----------------------------------------------------------').grid()
tkinter.Label(root,text = '-----------------------------------------------------------').grid()
titl2 = tkinter.Label(root, text = 'Username Generator', font = ('Arial',25)).grid()
tkinter.Label(root,).grid()
genuserbut = tkinter.Button(root,text = 'Generate Username', command = usergen1,font= ('unispace',8),bg = 'light green').grid()
tkinter.Label(root,).grid()
tkinter.Entry(root,textvariable = user).grid()
tkinter.Label(root,).grid()

copyuserbut = tkinter.Button(root,text = 'Copy Username',command = lambda:copy_user(usern),font=('unispace',8),bg = 'light blue').grid()
root.mainloop()
