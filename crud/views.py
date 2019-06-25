from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Person

# Create your views here.
@login_required
def index(request):
    return render(request, 'crud/index.html')

@login_required
def search(request):
    return render(request, 'crud/search.html')

@login_required
def create(request):
    context = {}
    if request.POST:
        name = request.POST["id_name"]
        date = request.POST["id_date"]
        number = request.POST["id_number"]
        p = Person(name=name, date=date, number=number)
        p.save()
        context["success"] = True
        context["Person"] = p
    return render(request, 'crud/create.html', context)