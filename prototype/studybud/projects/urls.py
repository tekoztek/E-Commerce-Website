from django.urls import path, register_converter
from . import views, converters

# app_name = 'base'

# register_converter(converters.Year_Month_Converter, 'yearmonth')



urlpatterns = [

    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),  # example of reading pk from url
    #form for adding new project to db
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
]
