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
    stickers = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['imageUrl', 'categoryName', 'stickers']

    def get_stickers(self, obj):
        data = {}
        for sticker in obj.stickers.all():
            category = sticker.category.name

            if category not in data:
                data[category] = []

            data[category].append({
                "sticker": sticker.image.url
            })

        return data

class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = ['image']