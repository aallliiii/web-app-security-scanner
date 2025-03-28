from django.urls import path
from django.views.generic import RedirectView
from file_checker import views

urlpatterns = [
    path('', views.home, name='upload_file'),
    path('upload/', views.upload_file, name='upload_file'),
    path('verify/', views.verify_file, name='verify_file'),
]
