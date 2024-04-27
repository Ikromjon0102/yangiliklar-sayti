from django.contrib import admin

# Register your models here.


from .models import News, Category, Contact


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','category','status', 'published_time']
    list_filter = ['category','status',]
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','body']
    date_hierarchy = 'published_time'
    ordering = ['published_time', 'status']




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Contact)