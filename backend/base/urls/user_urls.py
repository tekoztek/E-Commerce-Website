from django.urls import path
from base.views import user_views as views



urlpatterns = [
    #path for obtaining access token
    # TokenObtainPairView - Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
    # to obtain the access token, we send post with username and password to this endpoint, built in
    # notice that TokenObtainPairView is customized in views.py as MyTokenObtainPairView
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('profile/', views.getUserProfile, name="users-profile"),
    path('', views.getUsers, name="users"),
    path('register/', views.registerUser, name="register"),
]
