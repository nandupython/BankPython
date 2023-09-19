from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('newpage', views.newpage, name='newpage'),
    path('branches/<int:district_id>/', views.get_branches_for_district, name='get_branches_for_district'),

]