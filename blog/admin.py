from django.contrib import admin
from blog.models import Post
# Register your models here


class Postadmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    fields=('title','content')
    list_display=('title','counted_views','status','published_date')
    list_filter=('published_date',)
    ordering_date=['created_date']
    search_fields=['title','content']
admin.site.register(Post,Postadmin)
