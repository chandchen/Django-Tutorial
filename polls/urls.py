from django.conf.urls import url

from . import views


urlpatterns = [
    # /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote/
    # regex:(?P<name>Experssion)  It's a capture group.
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
