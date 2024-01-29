from django.urls import path
from .views import restricted_view

urlpatterns = [
    # ... inne trasy
    path('restricted/', restricted_view, name='restricted'),
]