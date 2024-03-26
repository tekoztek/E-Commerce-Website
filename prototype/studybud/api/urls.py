from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # generate a token, based on the user
    TokenRefreshView, # token, to generate a new token - simple token expires in 5 min, every time token expires we send refresh token to get new token
)

urlpatterns = [
    # all token views are provided by the library
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('project/<str:pk>', views.getProject),
    path('projects/<str:pk>/vote/', views.projectVote),
]




