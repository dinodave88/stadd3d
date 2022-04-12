from django.urls import path, include
from . import views

app_name = 'stadd3d'

urlpatterns = [
    path('', views.home_3D, name='App1'),
    path('run', views.run_3D, name='run_3D')
]
