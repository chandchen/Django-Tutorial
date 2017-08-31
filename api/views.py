from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.models import Question, Choice

from .serializers import UserSerializer, QuestionSerializer, ChoiceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# class QuestionList(APIView):
#
#     def get(self, request, format=None):
#         question = Question.objects.all()
#         serializer = QuestionSerializer(question, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceList(APIView):

    def get_object(self, pk):
        try:
            question = Question.objects.get(pk=pk)
            return Choice.objects.filter(question=question)
        except Choice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = Question.objects.get(pk=pk)
        choice = Choice.objects.filter(question=question)
        serializer = ChoiceSerializer(choice, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = Question.objects.get(pk=pk)
        choice = Choice.objects.filter(question=question)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def choice_list(request, pk):
    try:
        question = Question.objects.get(pk=pk)
        choices = Choice.objects.filter(question=question)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.question = question
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        choices.delete()
        return HttpResponse(status=204)
