from django.contrib import admin 
from .models import Movie,Cast

# Register your models here. 
class CastAdmin(admin.ModelAdmin):
     list_display=['id','name','gender','dob']
admin.site.register(Cast,CastAdmin)  

class MovieAdmin(admin.ModelAdmin):
    list_display=['id','title','cast','created_at','updated_at','runtime','language','tagline'] 
admin.site.register(Movie,MovieAdmin)  

  