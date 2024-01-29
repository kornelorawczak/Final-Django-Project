from django.urls import path
from .views import login_view, custom_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
]