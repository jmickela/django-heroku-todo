from django.conf.urls import include, url
from django.contrib import admin

from api.apiv1 import router

urlpatterns = [
    # Examples:
    # url(r'^$', 'todoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]