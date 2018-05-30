"""
    Snippets URL Configuration

"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetListCreateView, SnippetRUDView, api_root, SnippetHighlight, UserListView, UserDetailView

app_name = 'snippets'

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),

    url(r'^snippets/$', SnippetListCreateView.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetRUDView.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='snippet-highlight'),

    url(r'^users/$', UserListView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail')
])