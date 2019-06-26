from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Person

# Create your views here.
@login_required
def index(request):
    return render(request, 'crud/index.html')

@login_required
def search(request):
    if request.GET and request.GET["search_str"]:
        people = Person.objects.filter(name__icontains=request.GET["search_str"])[:5]
    else:
        people = Person.objects.all()[:5]
    return render(request, 'crud/search.html', context={"people" : people})

@login_required
def create(request, id=None, success=None):
    context = {}
    if request.POST:
        name = request.POST["id_name"]
        date = request.POST["id_date"]
        number = request.POST["id_number"]
        submit = request.POST["btn_submit"]
        _id = request.POST["id_person"]
        if submit == "Delete":
            Person.objects.get(id=_id).delete()
            print("deleting")
            return redirect('crud:create')
        if _id and submit != "Delete":
            p = Person.objects.get(id=_id)
            p.name = name
            p.date = date
            p.number = number
            p.save()
            return redirect('crud:create', id=p.id, success=1)
        p = Person(name=name, date=date, number=number)
        p.save()
        return redirect('crud:create', id=p.id, success=1)
    elif id:
        p = get_object_or_404(Person, id=id)
        context["Person"] = p
        if success:
            context['success'] = True
    return render(request, 'crud/create.html', context)