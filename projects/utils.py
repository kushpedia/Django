from django.db.models import Q
from .models import Tag, Project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProjects(request, projects,results):

    page = request.GET.get('page')
    paginator = Paginator(projects,results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page)- 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+ 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects

def searchProject(request):
    search_querry = ''

    if request.GET.get('search_querry'):
        search_querry = request.GET.get('search_querry')

    tag = Tag.objects.filter(name__icontains=search_querry)

    projects = Project.objects.distinct().filter(Q(title__icontains = search_querry)|
                                                Q(tags__in=tag)|
                                                Q(description__icontains=search_querry)|
                                                Q(owner__name__icontains=search_querry))

    return projects,search_querry
