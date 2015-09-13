from django.contrib import admin

# Register your models here.
from .models import Blog
from .models import Comment


class BlogAdmin(admin.ModelAdmin):
    fields = ("Name", "Email", "Title", "content",)
    list_display = ('upper_case_name', "content", "Email", "Title",'pub_date','edited_date',)

    def upper_case_name(self, obj):
        return obj.Name.upper()
    upper_case_name.short_description = 'Name'
admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    fields = ("blog", 'comment_content',)
    list_display = ('blog', 'comment_content','pub_date','edited_date')
admin.site.register(Comment, CommentAdmin)
