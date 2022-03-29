from django.contrib import admin
from app.models import Articles #文章表
from app.models import Tags #标签表
from app.models import Cover #文章封面表

# Register your models here.

admin.site.register(Articles)
admin.site.register(Tags)
admin.site.register(Cover)