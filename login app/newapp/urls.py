from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup),
    path('add',views.add),
    path('verify',views.verify),
    path('logout',views.logout),
    path('login',views.login),
    path('home',views.home),
    path('signup',views.signup)
    
]

