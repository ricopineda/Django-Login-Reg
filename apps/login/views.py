from __future__ import unicode_literals
from models import *
from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):

	return render(request,'login/index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
            return redirect('/')
        else:
            users = User.objects.filter(email=request.POST['email'])
            if len(users):
                messages.error(request,"This email is already in use!")
                return redirect('/')
            else:
				users = User.objects.create(first_name=fname, last_name=lname, email=email, password=password)
				request.session['id'] = users.id
				return redirect('/home')
    else:
        return redirect('/')


def login(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.all().filter(email=email)
		if len(user):
			if user[0].password == password:
				request.session['id'] = user[0].first_name

				return redirect('/home')
		return redirect ('/')		

def logout(request):

	request.session['id'] = 0
	return redirect('/')

def home(request):

	return render(request, 'login/home.html')

