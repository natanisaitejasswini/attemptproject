from django.shortcuts import render,redirect, HttpResponse
from ..loginapp.models import Userlog
from .models import Appt
from django.contrib import messages 
from datetime import datetime
from django.core.urlresolvers import reverse
import bcrypt
def user(request):
	errors = False
	check1 = Appt.UserManager.task(request.POST['task'])
	check2 = Appt.UserManager.date_check(request.POST['appdate'])
	check3 = Appt.UserManager.time_check(request.POST['time'])
	# Errors Route
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid Task", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Invalid Date", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid Time", extra_tags="regtag")
		errors = True
	if errors == True:
		return redirect('/appointments')
	elif (check1[0] == True & check2[0] == True & check3[0] == True):
		users = Userlog.objects.get(name = request.session['user'])
		Appt.objects.create(user = users ,task=check1[1], date=check2[1], time=check3[1], status='pending')
		return redirect('/appointments')
def edit(request, task_id):
	context = {
		'updates' : Appt.objects.filter(id=task_id)
	}
	return render(request, 'attemptapp/show.html', context)
def update(request, task_id):
	app_update = Appt.UserManager.Update(task_id, request.POST)
	if app_update[0] == False:
		for error in app_update[1]:
			messages.add_message(request, messages.INFO, error)
		return redirect(reverse('gohere',kwargs={'task_id' : task_id}))
	else:
		return redirect('/appointments')
def destroy(request, task_id):
	Appt.objects.get(id=task_id).delete()
	return redirect('/appointments')


