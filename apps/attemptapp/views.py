from django.shortcuts import render,redirect, HttpResponse
from ..loginapp.models import Userlog
from django.contrib import messages 
from datetime import datetime
import bcrypt


