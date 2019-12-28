from django.contrib import admin
from myapp.models import *
# Register your models here.
class TopicAdminView(admin.ModelAdmin):
    list_display=('top_name',)
class WebpageAdminView(admin.ModelAdmin):
    list_display=('top_name',"name","url")#what to display to admin
    list_per_page=5 #No of records per page
    list_editable=('name','url')
    search_fields=("name",)
    list_filter=('top_name',)

admin.site.register(Topic,TopicAdminView)
admin.site.register(Webpage,WebpageAdminView)
admin.site.register(Access_Details)