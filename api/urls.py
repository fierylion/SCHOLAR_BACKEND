from django.urls import path
from .views import getResults, home, getPostLecturers
urlpatterns = [
  path(r'results',getResults ),  
  path(r'lecturers', getPostLecturers),
  path(r'', home)
]