from django.urls import path
from .views import Quiz, RandomQuestionTopic, StartQuiz, NormalQuestionTopic
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    #path('q/', Question.as_view(), name='question'),
    #path('a/', Answer.as_view(), name='answer'),
    path('r/<str:topic>/', RandomQuestionTopic.as_view(), name='RandomQuestionTopic'),
    path('single/<str:title>/', StartQuiz.as_view(), name='quiz'),
    path('total-questions/', views.Quiz.get_total_questions, name='get_total_questions'),
    path('n/<str:topic>/', NormalQuestionTopic.as_view(), name='NormalQuestionTopic'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)