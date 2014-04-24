#!/usr/bin/python
import sys

#creating a global dictionary
Users = dict()
dictkey = 0
#procedure to read user data and fill in Users dictionary
def useradd():
	global dictkey
	list = []
	listparam = raw_input('enter user name: ')
	list.append(listparam)
	listparam = raw_input('enter user place: ')
	list.append(listparam)
	listparam = raw_input('enter user DOB in ddmmyyyy: ')
	list.append(listparam)
	dictkey = dictkey + 1
	Users[dictkey]=[list]

#procedure to display Users dict:
def pritnusers():
    for k,v in Users.iteritems():
        print k, " : ",v
        
#create a global dictionary for Aquaintances mapping userid against one or more friend ids.
Acquaintances = dict()
#procedure to read aquaintance data and fill in Acquaintances dictionary
def add_friends(user_id,friend_id):

#add a function to get userif from username:
>>> for k, v in Users.iteritems():
...     if(Users[k][0][0]=='krishna'):
...         print k,v

#>>> Users
#{1: [['sai', 'rjy', '17061989']], 2: [['krishna', 'rjy', '17061989']]}
#add a function to read userid and friendid from user.
    list = []
    listparam = raw_input('enter userid : ')
    list.append(listparam)
    listparam = raw_input('enter friendid: ')
    list.append(listparam)
    dictkey = dictkey + 1
    Users[dictkey]=[list]

useradd()
useradd()
pritnusers()

