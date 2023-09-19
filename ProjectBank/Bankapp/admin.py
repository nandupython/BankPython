from django.contrib import admin
from . models import UserProfile
from .models import District, Branch
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(District)
admin.site.register(Branch)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district',)