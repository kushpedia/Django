from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Skill
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from .utils import searchProfiles, paginateProfiles

# Create your views here.
def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request,profiles,3)


    context = {'profiles':profiles, 'search_querry':search_query,'custom_range':custom_range }

    return render(request, 'users/profiles.html', context)


# access user profile
# @login_required(login_url='login')
def user_profile(request,pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description = "")


    context = {'profiles':profile, 'top_skills':top_skills, 'other_skills':other_skills}

    return render(request, 'users/user-profile.html', context)


# login user
def loginUser(request):
    page = "login"
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.info(request, "Username Does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect (request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, "Wrong Username OR Password!")

    return render(request, 'users/login_register.html',context)


# logout user
def logoutUser(request):
    logout(request)
    messages.info(request, "User Logged Out Succesfully")
    return redirect('login')

# user registration
def userRegistration(request):
    form = CustomUserCreationForm()
    page = "register"
    context = {'page': page, 'form':form}
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User Created Succesfully")
            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, "User Creation Failed.")
    return render(request, 'users/login_register.html', context)


# user Account:
@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'projects':projects, 'skills':skills}
    return render(request, 'users/account.html', context)


# edit account
@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}

    return render(request, 'users/profile_form.html', context)



# create Skills
@login_required(login_url='login')
def createSkill(request):   
    
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill created successfuly")
            return redirect('account')
            
    context = {'form':form}
    return render(request, 'users/skill_form.html', context)
    

# edit skills
@login_required(login_url='login')
def editSkill(request,pk):
    profile = request.user.profile

    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated successfuly")
            return redirect('account')

    context = {'skill': skill, 'form': form}

    return render(request, 'users/skill_form.html',context)

@login_required(login_url="login")
def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill deleted successfuly")
        return redirect('account')

    context= {'object': skill}
    return render(request, 'delete.html', context)

@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = profile.messages.filter(is_read=False).count()
    context = {'messageRequests':messageRequests,'unreadCount':unreadCount }
    return render(request, 'users/inbox.html', context)

@login_required(login_url="login")
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {'message':message}
    return render(request, 'users/message.html', context)

def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()   
            messages.success(request, "Message sent  successfuly")
            return redirect('user_profile', pk=recipient.id)


    context = {'recipient':recipient, 'form':form}
    return render(request, 'users/message_form.html', context)
