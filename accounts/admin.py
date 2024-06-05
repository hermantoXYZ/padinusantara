from django.contrib import admin
from .models import User, Stats, PostNews, Media, Contact, Page, Program, Buku
from tinymce.widgets import TinyMCE
from django.db import models






class PostNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category')
    search_fields = ('title', 'author__username', 'category')
    list_filter = ('created_at', 'category')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    
    # Menentukan TinyMCE untuk field content
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class MediaAdmin (admin.ModelAdmin):
    list_display = ('title', 'content','images', 'url_drive')

class ProgramAdmin (admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'harga', 'ISBN', 'berat')
    search_fields = ('judul', 'ISBN')

admin.site.register(User)
admin.site.register(Stats)


admin.site.register(PostNews, PostNewsAdmin)
PostNews._meta.verbose_name_plural = "Post News"

admin.site.register(Media, MediaAdmin)
Media._meta.verbose_name_plural = "Media"

admin.site.register(Contact)
Contact._meta.verbose_name_plural = "Contact Person"

admin.site.register(Page)
Page._meta.verbose_name_plural = "Halaman"

admin.site.register(Program, ProgramAdmin)
Program._meta.verbose_name_plural = "Program"

admin.site.register (Buku, BukuAdmin)
Buku._meta.verbose_name_plural = "Buku"