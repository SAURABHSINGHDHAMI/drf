from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):

    courses = {
    'course_name' : 'Python',
    'course_topics' : ['Flask', 'Django', 'Tornado', 'FastAPI'],
    'course_provider' : 'harvard'
    }

    if request.method == 'GET':
        print('YOU HIT A GET METHOD')
        return Response(courses)
    elif request.method == 'POST':
        print('YOU HIT A POST METHOD')
        return Response(courses)
    elif request.method == 'PUT':
        print('YOU HIT A PUT METHOD')
        return Response(courses)
    elif request.method == 'PATCH':
        print('YOU HIT A PATCH METHOD')
        return Response(courses)