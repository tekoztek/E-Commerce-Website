from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser # return bool, used ind authorizaiton decorator
from rest_framework.response import Response


from django.contrib.auth.models import User

from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

# imports for customizing token encoded data
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status # for status codes in responses



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # setting additional fields to token encoded data
    '''@classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['message'] = 'Hello, World!'
        # ...

        return token'''
    # a way to return additional in response with tokens - used to ease the login functionality
    def validate(self, attrs):
        #list with data to return in jwstoken
        data = super().validate(attrs)
        
        '''data['username'] = self.user.username
        data['email'] = self.user.email'''

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# view that registers user and return information about its account, including token
@api_view(['POST'])
def registerUser(request):
    data = request.data # get data from sent body
    try: 
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password']) # hash password
        ) # crete user and store access to it in varibale
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user # determines what user does request. Information is fetched from sent token
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

#admin specific url to get all users
@api_view(['GET'])
@permission_classes([IsAdminUser]) # no need to add isauthenticated, because has to be auth to be admin
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
