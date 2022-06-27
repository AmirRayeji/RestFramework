from rest_framework.generics import ListCreateAPIView

from .serializers import ArticleSerializer
from blog.models import Article

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
