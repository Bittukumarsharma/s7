from django.shortcuts import render 
from .serializers import CastSerializer,MovieSerializer
from rest_framework import viewsets 
from .models import Cast,Movie 
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Create your views here.
class CastViewSet(viewsets.ModelViewSet):
    queryset=Cast.objects.all()
    serializer_class=CastSerializer
    authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[AllowAny] 
    permission_classes=[IsAdminUser]


class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[AllowAny] 
    permission_classes=[IsAdminUser]
