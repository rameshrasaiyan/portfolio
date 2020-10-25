from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path("<int:pk>", views.project_details, name='project_details'),
]