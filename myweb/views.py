from django.shortcuts import render,redirect, get_object_or_404
from .models import Branch ,Field, Topic, Resource

def home(request):
    cat=Field.objects.all()
    return render(request, 'home.html', {'cat':cat})

def fields(request, pk):
    fields = get_object_or_404(Field, pk=pk)
    branch = Branch.objects.filter(field=fields)
    return render(request, 'fields.html', {'fields': fields, 'branch': branch})

def branches(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    topics = Topic.objects.filter(branch=branch)
    return render(request, 'branch.html', {'topics': topics, 'branch': branch})
def topics(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'topics.html', {'topic': topic})