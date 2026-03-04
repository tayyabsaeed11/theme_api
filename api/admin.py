from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Theme, Story


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    ordering = ('name',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'isPremium',
        'downloads',
        'sortOrder',
        'createdAt'
    )

    list_filter = ('isPremium', 'category')
    search_fields = ('id', 'name')
    ordering = ('sortOrder',)
    list_editable = ('isPremium', 'downloads', 'sortOrder')
    list_per_page = 20


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('imageUrl', 'category')
    list_filter = ('category',)
    search_fields = ('category__name',)