"""
    REST URL Configuration

"""

from django.conf.urls import url, include
from django.contrib import admin

from snippets.views import UserDetailView, UserListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^auth/', include('rest_framework.urls')),

    url(r'^', include('snippets.urls')),
]
