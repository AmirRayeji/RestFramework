from django.urls import path, include

from .views import UserViewSet, ArticleViewSet

from rest_framework import routers

app_name='api'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
]