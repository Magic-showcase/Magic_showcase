from django.contrib import admin
from .models import Users
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model=Users
    readonly_fields=('Created','Update')
    list_display=['user','country','bio']
    search_fields=('user','birth')
    list_filter=('country','Created','Update')


admin.site.register(Users,UserAdmin)
