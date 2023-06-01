from django.shortcuts import render,redirect
from database.models import Person, PersonForm

def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid :
            form.save()
    else : 
        form = PersonForm()
    
    data = {'form' : form}
    return render (request, "person_create.html", data)

def person_read(request) :
    persons = Person.objects.all
    data = {'persons' : persons}
    return render(request, "person_read.html", data)

def person_update(request, id) : 
    row = Person.objects.get(id = id)
    if request.method ==  "POST" : 
        form = PersonForm(instance = row, data = request.POST) 
        if form.is_valid() :
            form.save()
    else :     
        form = PersonForm(instance = row)

    data = {'form' : form}
    return render (request, "person_update.html", data)

def person_delete(request , id) :
    Person.objects.get(id = id).delete()
    return redirect('person_read')