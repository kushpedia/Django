from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .utils import searchProject, paginateProjects
# Create your views here.


def projects(request):
    projects,search_querry = searchProject(request)

    custom_range,projects = paginateProjects(request,projects,6)

    context = { "allproject": projects,"search_querry":search_querry, 'custom_range':custom_range}

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    form = ReviewForm()
    projectObject = Project.objects.get(id=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.project = projectObject
        review.save()
        projectObject.getVoteCount
        messages.success(request, "Review submitted successfuly")
        return redirect('project', projectObject.id)


    
    context = {"currentProject":projectObject, 'form':form}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").replace('.', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project= form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            messages.success(request, "Project created successfuly")
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").replace('.', " ").split()
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            messages.success(request, "Project Updated successfuly")
            return redirect('account')

    context = {'form': form, 'project':project}
    return render(request, 'projects/project_form.html', context)    

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfuly")
        return redirect('account')
    context = {"object":project}
    return render(request, 'delete.html', context)


