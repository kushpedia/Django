from django.db.models import Q
from .models import Skill, Profile

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfiles(request, profiles,results):

    page = request.GET.get('page')
    paginator = Paginator(profiles,results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page)- 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+ 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles

def searchProfiles(request):
    search_querry = ''
    if request.GET.get('search_querry'):
        search_querry = request.GET.get('search_querry')

    skill = Skill.objects.filter(name__icontains=search_querry)

    profiles = Profile.objects.distinct().filter(Q(name__icontains =search_querry)|
                                        Q(short_intro__icontains=search_querry)|
                                        Q(skill__in=skill))
    return profiles,search_querry