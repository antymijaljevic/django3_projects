from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(string.ascii_uppercase)
    
    if request.GET.get('numbers'):
        characters.extend(string.digits)

    if request.GET.get('special'):
     characters.extend(list('@#!<>/\|'))

    length = int(request.GET.get('length', 5)) #5 is default value
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html',{'password':thepassword})
