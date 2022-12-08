from django.contrib import admin

# Register your models here.
from .models import Video, CodeFile
admin.site.register(Video)
admin.site.register(CodeFile)
