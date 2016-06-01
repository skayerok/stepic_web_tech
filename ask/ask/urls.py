from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views
from qa import views
admin.autodiscover()

0
urlpatterns = [
    url(r'^$', views.question_list, name="question_list"),
    url(r'^answer/', views.add_answer),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login_user, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^question/(?P<question_id>[0-9]+)/', views.question_details, name="question_details"),
    url(r'^ask/', views.question_add, name="question_add"),
    url(r'^popular/', views.question_list, name="question_popular"),
    url(r'^new/', views.test),
]
