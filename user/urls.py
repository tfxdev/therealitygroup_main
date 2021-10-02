from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='Login'), 
    path('register/', views.Register, name='Register'),
    path('dashboard/', views.Dashboard, name='Dashboard'),
  #  path('dashboard/love', views.Love, name='Love'),
  #  path('dashboard/settings', views.Account_settings, name='Account_settings'),
  #  path('dashboard/messages', views.Messages, name='Messages'),
    path('logout/', views.Logout, name='Logout'),



]