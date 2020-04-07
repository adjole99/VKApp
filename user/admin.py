from django.contrib import admin
from .models import user,Task,Advices
# Register your models here.
admin.site.register(user)
admin.site.register(Task)
admin.site.register(Advices)