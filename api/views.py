from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project

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