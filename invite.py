import hashlib
import binascii
import string
import sys
import random
print('\nWelcome to Invite Text the World')
print('© 2019-2020 Hologram Inc.')
choice= input('Would you like to a) log in or b) sign up ')
the_first={}
the_last={}
the_users={}
the_pswd={}
the_names={}
the_usranames={}
the_usraname={}
the_usranam={}
the_usrana=[]
the_usran=[]
def read1():
    with open('texts.txt',"r") as file:
      for line in file:
        global user
        receiver,sender,message,code,number,status=line.split('!88!')
        if receiver == hashlib.md5(user.encode('utf-8')).hexdigest() or sender== hashlib.md5(user.encode('utf-8')).hexdigest():
          the_usranames[receiver]=sender
          the_usraname[message]=sender
          q=list(code.split(','))
          the_usranam[message]=q
          t=list(message)
          the_usrana.append(message)
          the_usran.append(status)

def read():
    with open ('users.txt') as f:
      for line in f:
        first,last,user,pswd,loginname,blank=line.split('!88!')
        the_first[user]=first
        the_last[first]=last
        the_users[user]=user
        the_pswd[user]=pswd
        the_names[user]=loginname
if choice.lower()=='b':
  read()
  print('Wonderful! Let\'s get you started!')
  loginname=input('What will be your login name(Remember people will just call you this. It is not a username. Dont make it personal.) ')
  firstname=input('What is your first name? ')
  lastname=input('What is your last name? ')
  username=input('What will be your username? ')
  while hashlib.md5(username.encode('utf-8')).hexdigest() in the_users or username=='q':
    username=input('Already Taken. What will be your username? ')
  password=input('What will be your password? ')
  print('Remember if you want to text someone you need their first name and username')
  cryptusra=hashlib.md5(username.encode('utf-8')).hexdigest()
  cryptpswd=hashlib.md5(password.encode('utf-8')).hexdigest()
  cryptfistname=hashlib.md5(firstname.encode('utf-8')).hexdigest()
  cryptlastname=hashlib.md5(lastname.encode('utf-8')).hexdigest()
  with open ('users.txt','a') as file:
    file.write(cryptfistname+'!88!'+cryptlastname+'!88!'+cryptusra+'!88!'+cryptpswd+'!88!'+loginname+'!88!'+'\n')
    choice='a1'
if choice=='a':
  read()
  print('Welcome Back')
  print('We will be asking for info shortly')
  user=input('What is your username... ')
  while hashlib.md5(user.encode('utf-8')).hexdigest() not in the_users:
    q= input('Oh no! That seems to be incorrect. Either type q to quit or r to retype your password in')
    while q=='q':
      print('Bye! We hope you make an account next time')
      sys.exit()
    while q=='r':
      user=input('Try Again.... ')
  if hashlib.md5(user.encode('utf-8')).hexdigest() in the_users:
    print('That seems to be correct')
    pswd=input('What is your password?... ')
    if the_pswd[hashlib.md5(user.encode('utf-8')).hexdigest()]==hashlib.md5(pswd.encode('utf-8')).hexdigest():
      read1()
      print('Great!')
      print('Hello')
      #print(the_usranames)
      #print(hashlib.md5(user.encode('utf-8')).hexdigest())
      if hashlib.md5(user.encode('utf-8')).hexdigest() in the_usranames:
        print('Yep')
        the_usra={}
        #print(the_usran)
        if 'Unread\n' in the_usran:
          print('Oooh new messages!')
          for i in range(len(the_usran)):
            if the_usran[i]=='Unread\n':
              print('New message... from',the_names[the_usraname[the_usrana[i]]])
              io=list(the_usrana[i])
              z=the_usranam[the_usrana[i]]
              u=1
              for i in range(128):
                io[int(z[len(z)-u])],io[int(z[len(z)-u-1])]=io[int(z[len(z)-u-1])],io[int(z[len(z)-u])]
                io[int(z[len(z)-u-2])],io[int(z[len(z)-u-3])]=io[int(z[len(z)-u-3])],io[int(z[len(z)-u-2])]
                del io[int(z[len(z)-u])]
                u+=4
              print('The message is:',''.join(io))
          print()
      text=input('Would you like to text someone? (yes or no) ')
      if text.lower()=='yes':
        print('Wonderful!')
        usaname= input('Can you please provide us the username of the person you\'re texting?')
        if hashlib.md5(usaname.encode('utf-8')).hexdigest() in the_users: 
          print('Yay! But we still need their first name')
          first= input('Please type in their first name ')
          if the_first[hashlib.md5(usaname.encode('utf-8')).hexdigest()] ==hashlib.md5(first.encode('utf-8')).hexdigest():
            print('WOOHOO!')
            y='yes'
            while y=='yes':
              print('Press q!2 to stop texting or otherwise just type your text in below and click enter when done')
              texts=input()
              if texts=='q!2':
                print('Oh you\'re done :(')
                y='no'
              else:
                Y=list(texts)
                C=list(texts)
                z=[]
                d={}
                f=1
                u=0
                io=C
                tysm=[]
                for i in range(128):
                  k=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits+ string.ascii_lowercase+ string.punctuation) for _ in range(1))
                #print(k)
                  if k==' ':
                    print('Oops')
                  while k==" ":
                    k=''.join(random.choice(string.printable) for 
                    i in range(1))
                    if k==' ':
                      print('Oops')
                    if k!=' ':
                      print('Great')
                  io.append(k)
                  tysm.append(k)
                  r=random.randrange(0,len(C)-1)
                  e=random.randrange(0,len(C)-1)
                  q=random.randrange(0,len(C)-1)
                  io[e],io[r]=io[r],io[e]
                  io[q],io[len(io)-1]=io[len(io)-1],io[q]
                  z.append(str(e))
                  z.append(str(r))
                  z.append(str(q))
                  z.append(str(len(io)-1))
                  f+=4
                  Z=','.join(z)
                  IO=''.join(io)
                #print(IO)
                #print(Z)
                #print(''.join(C)
                with open ('texts.txt', 'a') as k:
                  k.write(hashlib.md5(usaname.encode('utf-8')).hexdigest()+'!88!'+hashlib.md5(user.encode('utf-8')).hexdigest()+'!88!'+IO+'!88!'+Z+'!88!'+'1'+'!88!'+'Unread'+'\n' )
                  print('Sent')
                  it=input('Would you like to stay signed in to wait for a possible message? (y or n)')
                  if it=='y':
                    print('Yeah yeah now you wont miss on a message from them!')
                    print('When anyone texts you you will see the message here')
                    while it=='y':
                      read1()
                      if 'Unread\n' in the_usran:
                        print('Oooh new messages!')
                        for i in range(len(the_usran)):
                          if the_usran[i]=='Unread\n':
                            print('New message... from',the_names[the_usraname[the_usrana[i]]])
                            io=list(the_usrana[i])
                            z=the_usranam[the_usrana[i]]
                            u=1
                            for i in range(128):
                              io[int(z[len(z)-u])],io[int(z[len(z)-u-1])]=io[int(z[len(z)-u-1])],io[int(z[len(z)-u])]
                              io[int(z[len(z)-u-2])],io[int(z[len(z)-u-3])]=io[int(z[len(z)-u-3])],io[int(z[len(z)-u-2])]
                              del io[int(z[len(z)-u])]
                              u+=4
                            print('The message is:',''.join(io))


