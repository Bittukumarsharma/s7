from rest_framework import serializers 
from .models import Movie,Cast


class CastSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cast 
        fields=['id','name','gender','dob'] 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields=['id','title','cast','created_at','updated_at','runtime','language','tagline']


