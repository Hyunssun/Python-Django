from django.urls import path

from . import views

urlpatterns = [
    path('question/<int:page_question_id>', views.question, name="detail"),
]
