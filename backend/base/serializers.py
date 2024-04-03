from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product


# turn querysets into the JSON format and selects which fields to include, and other properties

class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField(read_only=True) # - put what you want to customize after get_
    _id = serializers.SerializerMethodField(read_only=True) 
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    #creating custom fields
    def get_isAdmin(self, obj): 
        return obj.is_staff
    
    def get__id(self, obj): 
        return obj.id


    def get_name(self, obj): 
        name = obj.first_name
        if name == '':
            name = obj.email
        return name
    
# to serialize user but with new token
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'