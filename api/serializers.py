from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import Question, Choice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:choice_list")

    class Meta:
        model = Question
        fields = ('url', 'question_text', 'pub_date')


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')
