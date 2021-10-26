from django.contrib import admin
from .models import Penguin, Swimming, Clothes

# Register your models here.
admin.site.register(Penguin)
admin.site.register(Swimming)
admin.site.register(Clothes)