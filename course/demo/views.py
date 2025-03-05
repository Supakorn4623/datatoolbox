from django.shortcuts import render
from .models import Course


def course_search(request):
    q = request.GET.get('q', '').strip()  
    courses = Course.objects.filter(course_name__icontains=q) if q else []  
    return render(request, 'course_list.html', {'q': q, 'courses': courses})