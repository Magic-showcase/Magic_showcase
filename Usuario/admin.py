from django.contrib import admin
from .models import Users
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model=Users
    readonly_fields=('Created','Update')
    list_display=['user']
    search_fields=('user','birth')

admin.site.register(Users,UserAdmin)
