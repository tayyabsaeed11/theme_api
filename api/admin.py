from django.contrib import admin
from .models import (
    Category,
    Theme,
    Story,
    Sticker,
    StickerCategory,
    StoryCategory,
    StoryTextImage
)

from django.utils.html import format_html


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
    list_display = ('id', 'category', 'preview')
    list_filter = ('category',)
    search_fields = ('category__name',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"


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


# ================= STORY CATEGORY =================
@admin.register(StoryCategory)
class StoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


# ================= INLINE TEXT IMAGES =================
class StoryTextImageInline(admin.TabularInline):
    model = StoryTextImage
    extra = 1  # how many empty fields show


# ================= STORY =================
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'preview', 'category')
    list_filter = ('category',)
    search_fields = ('category__name',)
    inlines = [StoryTextImageInline]

    def preview(self, obj):
        if obj.imageUrl:
            return format_html('<img src="{}" width="60"/>', obj.imageUrl.url)
        return "-"
    preview.short_description = "Preview"