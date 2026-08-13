from django.contrib import admin

# Register your models here.
from .models import Branch,Field, Resource,Topic
admin.site.register(Field)
admin.site.register(Branch)
admin.site.register(Topic)
admin.site.register(Resource)