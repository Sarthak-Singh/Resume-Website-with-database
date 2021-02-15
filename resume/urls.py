from django.urls import path
from .views import resumeView

urlpatterns = [
    path('', resumeView, name='resume-base'),
]
