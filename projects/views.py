from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
from django.http import HttpResponse




def projects(request):
    projects = Project.objects.all()
    context = { "allproject": projects}

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    
    context = {"currentProject":projectObject}
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect ('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)    


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {"project":project}
    return render(request, 'projects/delete.html', context)