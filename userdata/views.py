from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm
from django.contrib import messages

from .models import Profile
from django.shortcuts import get_object_or_404
from .forms import UserForm2 , ProfileForm2

# Create your views here.
def home(request):
    pass

def register(request)    :
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/notes')
    else:
        form = UserCreationForm()
    context = {
    'form': form ,
    }
    return render(request, 'signup.html', context )


def profile(request , slug ):
    #v_profile= Profile.objects.get(slug=slug) # اسم الجدول
    v_profile=get_object_or_404(Profile, slug=slug)
    context = {
        'profile': v_profile
    }
    return render(request , 'profile.html' , context)

def edit_profile(request , slug):
    v_profile=get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        v_user_form = UserForm2(request.POST , instance = request.user) # اسم الفورم
        v_profile_Form = UserForm2(request.POST , request.FILES , instance = v_profile) # اسم الفورم
        if v_user_form.is_valid() and v_profile_Form.is_valid() :
            v_user_form.save()
            v_profile_Form.save()
            # v_profile_Form2 = v_profile_Form.save(commit = False)
            # v_profile_Form2.user=request.user
            # v_profile_Form2.save()
            messages.success(request, 'Your Profile Updated successfull')
            return redirect('/')
        pass
    else:
        v_user_form = UserForm2(instance = request.user)
        v_profile_Form = ProfileForm2(instance=v_profile)
    context = {
        'userform' : v_user_form ,
        'profileForm' : v_profile_Form
    }
    return render(request ,'edit_profile.html', context)

def change_password(request , slug):
    v_profile=get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        v_password_form = PasswordChangeForm(request.user  , request.POST)
        if v_password_form.is_valid():
            v_password_form.save()
            return redirect('/')
    else:
        v_password_form = PasswordChangeForm(request.user)
    context = {
        'password_form' : v_password_form,

    }
    return render(request ,'password_form.html', context)
