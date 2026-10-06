from django.contrib import admin
from website.models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    fields=('title','content','status')
    list_display=('name','email','created_date')
    list_filter=('email',)
    
    search_fields=['title','content']
admin.site.register(Contact,ContactAdmin)