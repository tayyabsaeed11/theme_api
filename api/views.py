from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Category, Story
from .serializers import CategorySerializer, StorySerializer


class ThemeDataAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        categories = Category.objects.all()
        stories = Story.objects.all()

        category_serializer = CategorySerializer(categories, many=True)
        story_serializer = StorySerializer(stories, many=True)

        return Response({
            "categories": category_serializer.data,
            "stories": story_serializer.data
        })