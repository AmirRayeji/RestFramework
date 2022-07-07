from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.models import Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='api:authors')

    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, value):
        filter_list = ['php', 'java', 'ruby']

        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("Don't use bad words! : {}".format(i))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
