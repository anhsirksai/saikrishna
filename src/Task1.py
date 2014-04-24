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
#for dkey,ulist in Users.items():
#	print "Userid: %d : " %(dkey,ulist)
def pritnusers():
	print Users
	#for k,v in dict.items():
	#	print k, " : ",v

useradd()
useradd()
pritnusers()

