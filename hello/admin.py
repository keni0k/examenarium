from django.contrib import admin

# Register your models here.
from .models import Greeting, Task


admin.site.register(Greeting)
admin.site.register(Task)