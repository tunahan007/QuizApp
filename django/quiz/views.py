from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Quizzes, Answer
from rest_framework import generics
from .serializers import QuizSerializer, RandomQuestionSerializer, AnswerSerializer, NormalQuestionSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404






class StartQuiz(APIView):

    def get(self, request, **kwargs):
        quiz = Quizzes.objects.filter(category__name=kwargs['title'])
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)


class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()
    
    @csrf_exempt
    def get_total_questions(request):
        total_questions = Question.objects.count()
        data = {
            'total_questions': total_questions,
        }
        return JsonResponse(data)
        #print(f"Total number of questions: {total_questions}")
        #return render(request, 'total-questions', total_questions)
    

class RandomQuestionTopic(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class NormalQuestionTopic(APIView):

    def get(self, request, format=None, **kwargs):
        question = questions = Question.objects.order_by('id')[:1]
        serializer = NormalQuestionSerializer(question, many=True)
        return Response(serializer.data)
    
    


