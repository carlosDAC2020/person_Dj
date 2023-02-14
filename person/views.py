from django.shortcuts import render, HttpResponse, redirect
from .models import Person

def index(request):
    return render(request,"person/index.html",{
        "persons":Person.objects.all()
    })

def add(request):
    new_person = Person.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        age = int(request.POST["age"])
    )
    new_person.save()
    return redirect("person:index")
    

    



def update(request, id_person):
    if request.method=="GET":
        return render(request, "person/detail.html",{
            "person": Person.objects.get(pk=id_person)
        })
    else:
        person_for_update = Person.objects.get(pk=id_person)
        person_for_update.first_name = request.POST["first_name"]
        person_for_update.last_name = request.POST["last_name"]
        person_for_update.age = int(request.POST["age"])
        person_for_update.save()
        return redirect("person:index")


def delete(request,id_person):
    person_for_delete = Person.objects.get(pk=id_person)
    person_for_delete.delete()
    return redirect("person:index")
