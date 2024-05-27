from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def index(request):

    if request.method == 'GET':
        json_response = {
            'name' : 'Programming',
            'language' : ['C++', 'Python'],
            'method' : 'GET'
        }

    else:
        data = request.data
        print(data)
        json_response = {
            'name' : 'Programming',
            'language' : ['C++', 'Python'],
            'method' : 'POST'
        }

    return Response(json_response)

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({'message' : 'success'})
    return Response(serializer.errors)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):

    if request.method == 'GET':
        obj = Person.objects.all()
        serializer = PersonSerializer(obj, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})
    
class PersonAPI(APIView):
    
    def get(self, request):
        obj = Person.objects.all()
        serializer = PersonSerializer(obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})
    
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.Get.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)
        serializer = PersonSerializer(queryset, many=True)
        return Response({'status' : 200, 'data' : serializer.data}, status=status.HTTP_204_NO_CONTENT)