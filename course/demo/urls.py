from django.urls import path
from .views import course_search  


urlpatterns = [
    path('', course_search, name='course_search'),  
]