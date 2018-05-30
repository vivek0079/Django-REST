"""
    REST URL Configuration

"""

from django.conf.urls import url, include
from django.contrib import admin

from snippets.views import UserDetailView, UserListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^', include('rest_framework.urls')),

    url(r'^snippets/', include('snippets.urls')),

    url(r'^users/$', UserListView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail'),
]
