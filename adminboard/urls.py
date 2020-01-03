from django.contrib import admin
from django.urls import path
from . import views

app_name = 'adminboard'
urlpatterns = [
    path('', views.adminlogin, name='adminlogin'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('logoutAdmin/', views.logoutAdmin, name='logoutAdmin'),
    path('adminuser/', views.adminuser, name='adminuser'),
    path('addcredential/', views.addcredential, name='addcredential'),
    path('postcred/', views.postcred, name='postcred'),
    path('admineditcand/<str:username>/', views.admineditcand, name='admineditcand'),
    path('admindelcand/<str:username>/', views.admindelcand, name='admindelcand'),
    path('adminnotifycand/<str:username>/', views.adminnotifycand, name='adminnotifycand'),
    path('addquest/', views.addquest, name='addquest'),
    path('viewquest/', views.viewquest, name='viewquest'),
    path('submission/', views.submission, name='submission'),
    path('delquest/<int:quest>/', views.delquest, name='delquest'),
    path('editquest/<int:quest>/', views.editquest, name='editquest'),
    path('changequest/', views.changequest, name='changequest'),
    path('candaction/<int:id>/', views.candaction, name='candaction'),
    path('bulkupload/', views.bulkupload, name='bulkupload'),
    path('other/', views.other, name='other'),
    path('delinstructions/<int:inst>/', views.delinstructions, name='delinstructions'),
    path('postinstructions/', views.postinstructions, name='postinstructions'),
]
