from django.urls import path
from .views import getResults, home
urlpatterns = [
  path(r'results',getResults ),
  path(r'', home)
]