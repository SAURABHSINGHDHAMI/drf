from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'course_topics' : ['Flask', 'Django', 'Tornado', 'FastAPI'],
        'course_provider' : 'harvard'
    }
    return Response(courses)