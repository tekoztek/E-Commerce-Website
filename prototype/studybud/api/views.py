from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review
from django.contrib.auth.models import User



@api_view(['GET'])
def getRoutes(request):
    
    # list will be turned into js array
    routes = [ 
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'}, # returns single project
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    
    
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    print('USER', request.user)
    projects = Project.objects.all()
    users = User.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    
    #print('DATA:', data)


    # either creates or returns the existing review, and stores them in one of according variables
    review, created = Review.objects.get_or_create(
        owner=user, # weird because user is attribute of project not, review
        project=project, # project that user left review for

    )

    review.value = data['value']
    review.save()
    
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)



