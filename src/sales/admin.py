from django.contrib import admin

# Register your models here.

from .models import Sale,Position,CSV

admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)