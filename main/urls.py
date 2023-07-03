from django.urls import path
from main.views import MyCreateViewSet,MyRetriveUpdateDestroyViewSet


urlpatterns = [
    path('api/',MyCreateViewSet.as_view(),name='api'),
    path('api/<int:pk>/',MyRetriveUpdateDestroyViewSet.as_view(), name='api1'),
    
]
