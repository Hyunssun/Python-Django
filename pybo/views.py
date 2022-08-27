from django.http import HttpResponse

from pybo.models import Answer, Question
from django.utils import timezone
from django.shortcuts import render


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


def question(request, page_question_id):
    q = Question.objects.get(id=page_question_id)
    q_context = {
        "id": q.id,
        "subject": q.subject,
        "content": q.content
    }

    a = Answer.objects.filter(question_id=page_question_id)
    a_context_list = a.values()

    context = {
        'q_context': q_context,
        'a_context_list': a_context_list
    }

    return render(request, 'pybo/question.html', context)
