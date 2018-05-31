from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.routers import DefaultRouter

# from .view import SnippetListCreateView, SnippetRUDView, api_root, SnippetHighlight, UserListView, UserDetailView
from .views import  SnippetViewSet, UserViewSet, api_root

app_name = 'snippets'

# Method 1 --> Adding Viewsets Using Routers

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]


# Method 2 --> Without Routers adding Viewsets

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ])


# Method 3 --> Class Based Views and their url patterns

# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),

#     url(r'^snippets/$', SnippetListCreateView.as_view(), name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetRUDView.as_view(), name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='snippet-highlight'),

#     url(r'^users/$', UserListView.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail')
# ])