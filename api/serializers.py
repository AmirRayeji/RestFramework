from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin

from blog.models import Article


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_author(self, obj):
        return obj.author.username

    author = serializers.SerializerMethodField('get_author')

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
