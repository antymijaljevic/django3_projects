from django.shortcuts import render #templates to find, needs dictionary
# from django.http import HttpResponse #return html only
from .models import Pet #import our class
from django.http import Http404

def home(request): #for home page
    # return HttpResponse('<p>Home view</p>')

    pets = Pet.objects.all() #query all attributes from class Pet
    return render(request, 'home.html', { #render template and dictionary
        'pets':pets,
    })

def pet_detail(request, pet_id):
    # return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')
    try:
        pet = Pet.objects.get(id=pet_id) #get pet by asked ID
    except Pet.DoesNotExist: #if id doesn't exist, return..
        raise Http404('Pet Not Found!')

    return render(request, 'pet_detail.html', {
        'pet': pet,
    })