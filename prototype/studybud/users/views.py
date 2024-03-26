from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm


def loginUser(request):
    page = 'login'
    # checks if user is authenticated, if so, doesn't allow to go to login page by redirecting to profiles page
    if request.user.is_authenticated:
        return redirect('profiles')
    


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        


        # if user exists, log in - create session in db, add it to browser cookies
        if user is not None:
            login(request, user)
            return redirect('profiles') # notice how url name is used rather than the actual url
        else: 
            
            messages.error(request, 'Username or password is incorrect')
        
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # creates an object automatically with provided data in form
        if form.is_valid():
            user = form.save(commit = False) # not just saving a form, but also initialize a user var with user object
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created successfully')

            login(request, user) # log in immediately after registration
            return redirect('edit-account')
        else: 
            messages.success(request, 'An error has occured during registration')

    context= {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context ={
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="") # esentilly jsut querries with conditions
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile # request.user is a user object, and user object has a profile object as one to one
    
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    
    
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form, }
    return render(request, 'users/profile_form.html', context)