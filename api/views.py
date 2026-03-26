from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Category, Story, Theme, Sticker
from .serializers import CategorySerializer, StorySerializer, ThemeSerializer


# ================= COMBINED API =================
class ThemeDataAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.prefetch_related('themes')
        stories = Story.objects.select_related('category').prefetch_related('textImages')

        return Response({
            "status": "success",
            "message": None,
            "data": {
                "categories": CategorySerializer(categories, many=True).data,
                "stories": StorySerializer(stories, many=True).data
            }
        })


# ================= CATEGORY =================
class CategoryListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()

        return Response({
            "status": "success",
            "message": None,
            "data": CategorySerializer(categories, many=True).data
        })


# ================= THEMES =================
class ThemeListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        themes = Theme.objects.select_related('category').order_by('sortOrder')

        return Response({
            "status": "success",
            "message": None,
            "data": ThemeSerializer(themes, many=True).data
        })


# ================= STORIES =================
class StoryListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stories = Story.objects.select_related('category').prefetch_related('textImages')

        return Response({
            "status": "success",
            "message": None,
            "data": StorySerializer(stories, many=True).data
        })

class StickerListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stickers = Sticker.objects.select_related('category')

        grouped_data = {}

        for sticker in stickers:
            category_name = sticker.category.name

            if category_name not in grouped_data:
                grouped_data[category_name] = []

            grouped_data[category_name].append({
                "sticker": sticker.image.url if sticker.image else None
            })

        return Response({
            "status": "success",
            "message": None,
            "data": grouped_data
        })