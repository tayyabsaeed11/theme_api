from django.urls import path
from .views import ThemeDataAPIView

urlpatterns = [
    path('data/', ThemeDataAPIView.as_view(), name='theme-data'),
]