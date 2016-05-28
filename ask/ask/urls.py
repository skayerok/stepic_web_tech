from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa import views
admin.autodiscover()


urlpatterns = [
    url(r'^$', views.question_list, name="question_list"),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(?P<question_id>[0-9]+)/', views.question_details, name="question_details"),
    url(r'^ask/', views.test),
    url(r'^popular/', views.question_list, name="question_popular"),
    url(r'^new/', views.test),
]
