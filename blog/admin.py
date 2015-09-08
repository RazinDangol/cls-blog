from django.contrib import admin

# Register your models here.
from .models import Blog
from .models import Comment



class BlogAdmin(admin.ModelAdmin):
    fields=("Name","Email","Title","content",'Pub_date')
    list_display=('upper_case_name',"content","Email","Title","pub_date")

    def upper_case_name(self,obj):
        return obj.Name.upper()
    upper_case_name.short_description = 'Name'
admin.site.register(Blog,BlogAdmin)


#admin.site.register(Blog.published())


admin.site.register(Comment)