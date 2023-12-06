from django.contrib import admin
from django.urls import path

from project1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.reg, name='register'),
    path('', views.index)
]
