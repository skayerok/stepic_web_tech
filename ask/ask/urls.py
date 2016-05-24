from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa import views
admin.autodiscover()

#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'ask.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    url(r'^admin/', include(admin.site.urls)),
#)

urlpatterns = [
    url(r'^$', views.test),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(?P<question_id>[0-9]+)/', views.test),
    url(r'^ask/', views.test),
    url(r'^popular/', views.test),
    url(r'^new/', views.test),
]
