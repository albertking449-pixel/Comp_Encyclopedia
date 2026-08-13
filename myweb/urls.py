from django.urls import path
from . import views
urlpatterns=[
    path('', views.home, name='home'),
    path('topics/<int:pk>/', views.topics, name='topics'),
    path('fields/<int:pk>/', views.fields, name='fields'),
    path('branches/<int:pk>/', views.branches, name='branches'),
]