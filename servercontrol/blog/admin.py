from django.contrib import admin
from blog.models import Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ('updated_at','title','content')
    search_fields = ('title',)
admin.site.register(Blog,BlogAdmin)
# Register your models here.
