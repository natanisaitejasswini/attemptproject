from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
from datetime import datetime
import bcrypt
Email_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def first_name(self,name):
		if not len(name) > 3:
			return(False,"Invalid Firstname") 
		else:
			return(True,name)
	def name_charcheck(self,name):
		if not name.isalpha():
			return(False,"Invalid characters")
		else:
			return(True,name)
	def user_name(self,alias):
		if not len(alias) > 3:
			return(False,"Invalid lastname") 
		else:
			return(True,alias)
	def reg_email(self,email):
		if not Email_REGEX.match(email):
			return(False,"Invalid email") 
		else:
			return(True,email)
	def password_charcheck(self,password):
		if not password.isalpha():
			return(False,"Password should have characters")
		else:
			return(True,"password")
	def password(self,password):
		if not len(password) > 5:
			return(False,"Invalid password") 
		else:
				# BCRYPT PASSWORD
			password = password.encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			return (True, hashed)
	def confirm_password(self,password,confirm_password):
		if not password == confirm_password:
			return(False,"confirm password")
		else:
			return(True,"password confirmed")
	def birthday(self,birthday):
		bday = birthday
		# Checking empty date field
		if bday == "":
			return(False, "Invalid Birthdate")
		now = datetime.now()
		print now
		
		# comparing datefield with today
		bday_test = datetime.strptime(birthday, '%Y-%m-%d')
		if bday_test > now:
			return(False, "Invalid Birthdate")
		else:
			return(True, birthday)
  	def log(self,email,password):
  		# print email, password
  		# users = self.all()
  		# for auser in users:
  		# 	print auser.email
  		# print self.filter(email=email)
  		try:
  			user = self.get(email = email)
  			# print user.password
  		except:
  			return (False, "User Does not Exist")
		password = password.encode()
		user_password = user.password.encode()
		print user_password
		if user and bcrypt.hashpw(password, user_password) == user_password:
			print user.name
			return (True, user.email)
		else:
			return (False, "Password doesnot match")	

class Userlog(models.Model):
  name = models.CharField(max_length=30)
  alias= models.CharField(max_length=30)
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=300)
  birthday = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  UserManager = UserManager()
  objects = models.Manager()











