from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(SocialLinks)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['photo','name','age','job']
    search_fields = ['name','age','job','technologies','languages']
    list_per_page = 10
admin.site.register(Visitors)
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['photo','title']
    list_per_page = 10
admin.site.register(Info)
admin.site.register(Xabarlar)