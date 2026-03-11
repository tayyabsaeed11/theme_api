from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Category, Story, Theme
from .serializers import CategorySerializer, StorySerializer, ThemeSerializer


class ThemeDataAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.prefetch_related('themes')
        stories = Story.objects.all()

        category_serializer = CategorySerializer(categories, many=True)
        story_serializer = StorySerializer(stories, many=True)

        return Response({
            "status": "success",
            "message": None,
            "data": {
                "categories": category_serializer.data,
                "stories": story_serializer.data
            }
        })

class CategoryListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response({
            "status": "success",
            "message": None,
            "data": serializer.data
        })


class ThemeListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)

        return Response({
            "status": "success",
            "message": None,
            "data": serializer.data
        })


class StoryListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)

        return Response({
            "status": "success",
            "message": None,
            "data": serializer.data
        })