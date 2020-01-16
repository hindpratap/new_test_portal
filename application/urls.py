from django.contrib import admin
from django.urls import path
from . import views

app_name = 'application'
urlpatterns = [
    path('', views.applogin, name='applogin'),
    path('signup/', views.appsignup, name='appsignup'),
    path('postsignup/', views.postsignup, name='postsignup'),
    path('logincand/', views.logincand, name='logincand'),
    path('instructions/', views.instructions, name='instructions'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('panel/', views.panel, name='panel'),
    path('submitted/', views.submitted, name='submitted'),
    path('forcelogout/<str:username>/', views.forcelogout, name='forcelogout'),
]
