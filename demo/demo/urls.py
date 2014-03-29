from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('demo.apps.home.urls')),
    url(r'^', include('demo.apps.ventas.urls')),
url(r'^media/(?P<path>,*)$','django.views.static.serve' ,{'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
