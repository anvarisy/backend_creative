from django.contrib import admin
from api.models import carousel, category, order, style, types, user

# Register your models here.
admin.site.register([category,style,user,order, types, carousel])