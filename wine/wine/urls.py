from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.urls')),
)
urlpatterns += patterns("django.views",
    url(r'^media(?P<path>.*)/$',
        "static.serve", {
        "document_root": settings.MEDIA_ROOT,
    })
)