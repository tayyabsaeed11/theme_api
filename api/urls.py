from django.urls import path
from .views import ThemeDataAPIView, ThemeListAPIView, StoryListAPIView, CategoryListAPIView, StickerListAPIView

urlpatterns = [
    path('fonts/', ThemeDataAPIView.as_view(), name='theme-data'),
    path('themes/', ThemeListAPIView.as_view(), name='themes'),
    path('stories/', StoryListAPIView.as_view(), name='stories'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('stickers/', StickerListAPIView.as_view(), name='stickers'),
]