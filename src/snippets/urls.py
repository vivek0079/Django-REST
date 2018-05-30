"""
    Snippets URL Configuration

"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetListCreateView, SnippetRUDView

app_name = 'snippets'

urlpatterns = [
    url(r'^$', SnippetListCreateView.as_view(), name='snippet-create'),
    url(r'^(?P<pk>[0-9]+)/$', SnippetRUDView.as_view(), name='snippet-rud'),

]

urlpatterns = format_suffix_patterns(urlpatterns)