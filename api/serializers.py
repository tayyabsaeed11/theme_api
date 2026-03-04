from rest_framework import serializers
from .models import Category, Theme, Story


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

    class Meta:
        model = Story
        fields = ['imageUrl', 'categoryName']