

from django.contrib import admin

from .models import Profolio ,category

# Register your models here.

class profolioAdmin (admin.ModelAdmin):
    list_display =["id","title","category",]






admin.site.register(Profolio ,profolioAdmin)
admin.site.register(category)
