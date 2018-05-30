from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

User = get_user_model()

class SnippetSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Snippet
        fields = [
            'id',
            'owner',
            'title',
            'url',
            'code',
            'line_nos',
            'language',
            'style'
        ]
        read_only_fields = ['id', 'url']
    
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'snippets',
        ]