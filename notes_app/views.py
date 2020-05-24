from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


## show all_notes
def all_notes(request):
    return HttpResponse('<h1> welcome all notes </h1>')

def note_detail(request):
    return HttpResponse('<h1> welcome one note </h1>')
