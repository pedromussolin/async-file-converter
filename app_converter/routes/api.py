from rest_framework import routers
from app_converter.views import FileTypeViewSet, ConversionViewSet, FileConvertView
from django.urls import path, include

api_router = routers.DefaultRouter()
api_router.register(r'file-types', FileTypeViewSet, basename='filetype')
api_router.register(r'conversions', ConversionViewSet, basename='conversion')

urlpatterns = [
    path('', include(api_router.urls)),
    path('convert/', FileConvertView.as_view(), name='file-convert'),
]
