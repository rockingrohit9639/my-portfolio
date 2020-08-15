from django.contrib import admin

# Register your models here.
from .models import Contact, Posts, BlogComment

admin.site.register(Contact)
admin.site.register(BlogComment)

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInjection.js',)