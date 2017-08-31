from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'questions', views.QuestionViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    # url(r'^question_list/$', views.QuestionList.as_view(), name='question_list'),
    # url(r'^choice_list/(?P<pk>[0-9]+)/$', views.ChoiceList.as_view(), name='choice_list'),
    url(r'^choice_list/(?P<pk>[0-9]+)/$', views.choice_list, name='choice_list'),
]
