from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Snippet
        fields = [
            'id',
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