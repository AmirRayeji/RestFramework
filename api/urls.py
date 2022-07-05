from django.urls import path, include

from .views import UserViewSet, ArticleViewSet

from rest_framework import routers

app_name='api'

router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]