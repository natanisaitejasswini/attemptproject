from django.shortcuts import render,redirect, HttpResponse
from .models import Userlog
from ..attemptapp.models import Appt
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
import bcrypt
def index(request):
	return render(request,'loginapp/index.html')
def success(request):
	now = datetime.now()
	context={
	'today': datetime.now().date(),
	'today_appt': Appt.objects.filter(Q(date__lte=now, date__gte=now) & Q(user__name=request.session['user'])).order_by('time'),
	'future_appt': Appt.objects.filter(Q(date__gte=now) & Q(user__name=request.session['user'])).exclude(date__lte=now, date__gte=now).order_by('date')
	}
	return render(request,'attemptapp/success.html',context)
def user(request):
	errors = False
	check1 = Userlog.UserManager.first_name(request.POST['name'])
	check2 = Userlog.UserManager.reg_email(request.POST['email'])
	check3 = Userlog.UserManager.password(request.POST['password'])
	check3_char = Userlog.UserManager.password_charcheck(request.POST['password'])
	check4 = Userlog.UserManager.confirm_password(request.POST['password'],request.POST['confirm_password'])
	check5 = Userlog.UserManager.birthday(request.POST['birthday'])
	
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid name", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Please provide email correctly", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid password", extra_tags="regtag")
		errors = True
	if check3_char[0] == False:
		messages.add_message(request, messages.INFO, "Invalid characters in password", extra_tags="regtag")
		errors = True
	if check4[0] == False:
		messages.add_message(request, messages.INFO, "Please confirm your password correctly", extra_tags="regtag")
		errors = True
	if check5[0] == False:
		messages.add_message(request, messages.INFO, "DateofBirth Field is incorrect", extra_tags="regtag")
		errors = True		    
	if Userlog.objects.filter(email = request.POST['email']):
	    messages.add_message(request, messages.INFO, "Email already registered!", extra_tags="regtag")
	    errors = True
	# Errors Route
	if errors == True:
		return redirect('/main')
	elif (check1[0] == True  & check2[0] == True & check3[0] == True & check5[0] == True):
		Userlog.UserManager.create(name=check1[1], password=check3[1], birthday=check5[1], email=check2[1])
		request.session['user'] = check1[1]
		return redirect('/appointments')

def login(request):
	check6 = Userlog.UserManager.log(request.POST['email'], request.POST['password'])
	if check6[0] == False:
		messages.add_message(request, messages.INFO, check6[1], extra_tags='logtag')
		return redirect('/main')
	else:
		request.session['user'] = check6[1]
		return redirect('/appointments')

def logout(request):
	del request.session['user']
	return redirect('/')






