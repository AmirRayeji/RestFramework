from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView

from .serializers import ArticleSerializer, UserSerializer, AuthorSerializer
from blog.models import Article
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperuserOrStaffReadOnly


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author']
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['status', 'publish']

    def get_permissions(self):
    
        if self.action in  ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)


class AuthorRetrieve(RetrieveAPIView):
    queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = AuthorSerializer
