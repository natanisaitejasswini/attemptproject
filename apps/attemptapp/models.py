from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime, timedelta, date, time
from time import strftime
from ..loginapp.models import Userlog
class UserManager(models.Manager):
	def task(self,task):
		if not len(task) > 1:
			return(False,"Invalid Description") 
		else:
			return(True,task)
	def date_check(self,appdate):
		appt_date = appdate
		today = strftime('%Y-%m-%d')
		if appt_date == "" or appt_date < today:
			return(False, "Invalid date")		
		return(True, appdate)
		
	def time_check(self,time):
		time_log = time
		if time_log == "":
			return(False, "Invalid time") 
		else:
			return(True, time)
	def Update(self, id, data):
		errors = []
		Appointment = Appt.objects.get(id=id)
		Appointment.task = data['task']
		Appointment.date = data['appdate']
		Appointment.time = data['time']
		Appointment.status = data['status']
		today = strftime('%Y-%m-%d')
		if data['appdate'] == "" or data['appdate'] < today:
			errors.append("Invalid Date")
		if data['time'] == "":
			errors.append("Invalid Time")
		if len(data['task']) < 1:
			errors.append("Invalid Task")
		if errors:
			return(False,errors)	
		if not errors:
			Appointment.save()
			return (True,Appointment)

class Appt(models.Model):
	user = models.ForeignKey('loginapp.Userlog', related_name='users')
	task = models.CharField(max_length=30)
	date = models.DateField()
	time = models.TimeField()
	status = models.CharField(max_length=30)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	UserManager = UserManager()
	objects = models.Manager()



