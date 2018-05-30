from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

User = get_user_model()

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    owner = serializers.CharField(read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name='snippets:snippet-highlight', format='html',)

    class Meta:
        model = Snippet
        fields = [
            'id',
            'owner',
            'title',
            'url',
            'code',
            'highlight',
            'line_nos',
            'language',
            'style'
        ]
        read_only_fields = ['id', 'url']
        extra_kwargs = {
            'url': {'view_name': 'snippets:snippet-detail'},
        }
    
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets:snippet-detail', read_only=True,)

    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'snippets',
        ]
        extra_kwargs = {
            'url': {'view_name': 'snippets:user-detail'},
        }