from django.urls import path
from . import views
urlpatterns = [
    path('',views.studentportfolio, name = 'details'),
]