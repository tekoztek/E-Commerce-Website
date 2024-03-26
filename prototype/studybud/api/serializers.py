from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False) # because otherwise the relationships will be returned as primary keys (ids)
    
    tags = TagSerializer(many=True) # one-to-many relationship
    reviews = serializers.SerializerMethodField() # many-to-one relationship in other way
    class Meta:
        model = Project
        fields = '__all__'

    # getting reviews for each project (one(project) to many(reviews) relationship), cause project don't contain reviews ids in them
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
    








