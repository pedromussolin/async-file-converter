from django.urls import path, include
from rest_framework import routers
from app_converter import views

router = routers.DefaultRouter()
router.register(r'file-types', views.FileTypeViewSet, basename='filetype')
router.register(r'conversions', views.ConversionViewSet, basename='conversion')

urlpatterns = [
    path('', include(router.urls)),
    path('convert/', views.FileConvertView.as_view(), name='file-convert'),
]
