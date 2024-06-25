from django.contrib import admin

from .models import posts,AllDataTypesModel,About  

admin.site.register(posts)
admin.site.register(AllDataTypesModel)
admin.site.register(About)
