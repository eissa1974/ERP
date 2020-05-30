from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from .models import Note
from .forms import NoteForm



## show all_notes
def all_notes(request):
##    return HttpResponse('<h1> welcome all notes </h1>')
    v_all_notes = Note.objects.all() # اسم الجدول
    context = {
        'all_notes' : v_all_notes
    }
    #return render(request,'all_notes.html' , context)
    return render(request,'notes.html' , context)

def detail(request , slug ):
    #return HttpResponse('<h1> welcome one note </h1>')
    v_note = Note.objects.get(slug=slug) # اسم الجدول
    context = {
        'note_detail': v_note
    }
    #return render(request , 'detail.html' , context)
    return render(request , 'one_note.html' , context)

def note_add(request):
    if request.method == 'POST':
        v_form = NoteForm(request.POST) # اسم الفورم

        if v_form.is_valid():
            new_form = v_form.save(commit = False)
            new_form.user=request.user
            new_form.save()
            messages.success(request, 'Note Created successfull')
            return redirect('/notes')

    else:
        v_form = NoteForm(request.POST) # اسم الفورم


    context = {
        'form' : v_form
        }
    return render(request , 'add.html' , context)

def note_edit(request, slug ):
    v_note = get_object_or_404(Note , slug=slug)
    if request.method == 'POST':
        v_form = NoteForm(request.POST , instance = v_note) # اسم الفورم
        if v_form.is_valid():
            new_form = v_form.save(commit = False)
            new_form.user=request.user
            new_form.save()
            messages.success(request, 'Note Updated successfull')
            return redirect('/notes')
    else:
        v_form = NoteForm(instance = v_note) # اسم الفورم
    context = {
        'form' : v_form
        }
    return render(request , 'edit.html' , context)
