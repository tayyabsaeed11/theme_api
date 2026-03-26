from rest_framework import serializers
from .models import Category, Theme, Story, Sticker


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    themes = ThemeSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'themes']


class StorySerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source='category.name')
    textImages = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['id','imageUrl', 'thumbnailUrl', 'categoryName', 'textImages']

    def get_textImages(self, obj):
        return [
            img.image.url if img.image else None
            for img in obj.textImages.all()
        ]

class StickerSerializer(serializers.ModelSerializer):
    sticker = serializers.SerializerMethodField()

    class Meta:
        model = Sticker
        fields = ['sticker']

    def get_sticker(self, obj):
        return obj.image.url if obj.image else None