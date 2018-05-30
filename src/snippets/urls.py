from django.conf.urls import url

from .views import snippet_list_or_create, snippet_detail

urlpatterns = [
    url(r'^snippets/$', snippet_list_or_create),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail)
]