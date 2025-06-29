from django.contrib import admin
from .models import Category,Blogs
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','created_at','update_at')
    ordering = ('id',) 
    


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','slug','author','blog_image','status','is_feacherd','created_at','update_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id','title','category__category_name','status') 
    list_editable = ('is_feacherd','status')  
    ordering = ('id',) 
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)

