from django.contrib import admin

from .models import Chair, Bed, Sofa
# Register your models here.

@admin.register(Chair, Bed, Sofa)

class ViewAdmin(admin.ModelAdmin):
    pass
