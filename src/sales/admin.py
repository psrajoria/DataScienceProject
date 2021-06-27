from django.contrib import admin
from django.db import models
# Register your models here.

from .models import Sale,Position,CSV

### Horizontal filter to choose or remove positions
class SaleAdmin(admin.ModelAdmin):
    filter_horizontal = ("positions",)

admin.site.register(Position)
admin.site.register(Sale,SaleAdmin)
admin.site.register(CSV)
