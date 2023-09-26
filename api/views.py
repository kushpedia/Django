from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag

@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'GET':'/api/projects'},
        {'POST':'/api/projects/id/vote'},


        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
        ]
    return Response(routes) 


@api_view(['GET'])
def getAllProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.filter(id=pk)
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)


# API FOR PROJECT VOTING

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,
    )

    review.value = data['value']
    review.save()
    project.getVoteCount

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    tag = Tag.objects.get(id=tagId)
    project = Project.objects.get(id=projectId)

    project.tags.remove(tag)
    return Response('Tag was Deleted')
