import json

from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from pip._vendor import requests
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        # beje reverse
        top_deals = Top_Deal.objects.all()
        category = Category.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'cars': cars , 'footer1': footer1, 'top_deals': top_deals, 'category': category}
        return render(request, 'index.html', context)


def rent(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'cars': cars , 'footer1': footer1}
        return render(request, 'rent.html', context)

def rent_form(request):
    if request.method == 'GET':
        id = request.GET['id']
        car = Car.objects.get(id=id)
        context = {'car':car}
        return render(request, 'rentform.html', context)
    elif request.method == 'POST':

        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = "6Lct418kAAAAANPKYbUL3soB-kyQFtwYd6InpxTa"
        cap_data = {"secret": cap_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)

def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    elif request.method == 'POST':

        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = "6Lct418kAAAAANPKYbUL3soB-kyQFtwYd6InpxTa"
        cap_data = {"secret": cap_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)

        contact = request.POST
        fullname = contact['fullname']
        email = contact['email']
        message = contact['message']

        if cap_json['success'] == False:
            user_error = 'Make sure you are not a robot'
            context = {'user_error': user_error}
            return render(request, 'contact.html', context)
        else:
            ContactForm = Contact(fullname=fullname, email=email, message=message)
            ContactForm.save()

        return HttpResponseRedirect('/message/')

def message(request):
    if request.method == 'GET':
        return render(request, 'message.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        register = request.POST
        name = register['name']
        surname = register['surname']
        email = register['email']
        password = register['password']
        confirmpassword = register['confirmpassword']
        username = name + ' ' + surname
        if User.objects.filter(username = username).exists():
            user_error = 'User exists'
            context = {'user_error': user_error}
            return render(request, 'login.html', context)
        elif User.objects.filter(email = email).exists():
            user_error = 'Email exists'
            context = {'user_error': user_error}
            return render(request, 'login.html', context)
        elif password == confirmpassword:

            # captcha_token = request.POST.get("g-recaptcha-response")
            # cap_url = "https://www.google.com/recaptcha/api/siteverify"
            # cap_secret = "6Lct418kAAAAANPKYbUL3soB-kyQFtwYd6InpxTa"
            # cap_data = {"secret": cap_secret, "response": captcha_token}
            # cap_server_response = requests.post(url=cap_url, data=cap_data)
            # cap_json = json.loads(cap_server_response.text)

            # if cap_json['success'] == False:
            #     user_error = 'Make sure you are not a robot'
            #     context = {'user_error': user_error}
            #     return render(request, 'register.html', context)

            user = User.objects.create(username=username, email=email, password=password)
            user.save()
            insertuser = RegisterUser(name=name, surname=surname, email=email, password=password)
            insertuser.save()
            return HttpResponseRedirect('/login_user/')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        login = request.POST
        username = login['username']
        password = login['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                user_error = 'User not active'
                context = {'user_error': user_error}
                return render(request, 'login.html', context)
        else:
            user_error = 'invalid input'
            context = {'user_error': user_error}
            return render(request, 'login.html', context)


def search(request):
    if request.method == 'GET':
        return render(request, 'rent.html')
    elif request.method == 'POST':
        search = request.POST
        pickup = search['pickup']
        returnplace = search['returnplace']
        pickupdate = search['pickupdate']
        returndate = search['returndate']


        return HttpResponseRedirect('/rent/')

