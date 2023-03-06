from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    path('messages/', views.messages, name='messages'),
    path('collections/', views.collections, name='collections'),
    path('users/', views.users, name='users'),
    path('settings/', views.settings, name='settings'),
    path('notifications/', views.notifications, name='notifications'),

]
