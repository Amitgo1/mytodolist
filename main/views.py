from django.shortcuts import render
from main.models import MyToDo
from main.serializers import MySerializers
from rest_framework import generics


class MyCreateViewSet(generics.ListCreateAPIView):
    queryset = MyToDo.objects.all()
    serializer_class = MySerializers
    
    
class MyRetriveUpdateDestroyViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyToDo.objects.all()
    serializer_class = MySerializers
    
    
def index(request):
    return render(request, 'main/index.html')

# Create your views here.
