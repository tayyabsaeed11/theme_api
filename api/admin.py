from django.contrib import admin
from .models import Category, Theme, Story, Sticker, StickerCategory


# ================= CATEGORY =================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    ordering = ('name',)


# ================= STICKER CATEGORY =================
@admin.register(StickerCategory)
class StickerCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


# ================= STICKER =================
@admin.register(Sticker)
class StickerAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('category__name',)


# ================= THEME =================
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


# ================= STORY =================
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'imageUrl', 'category')
    list_filter = ('category',)
    search_fields = ('category__name',)
    filter_horizontal = ('stickers',)