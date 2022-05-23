from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Player, Category, Question, Answer
from .forms import AjaxForm

import json

@login_required
def get_questions(request, category_pk):
    questions = Question.objects.filter(category=category_pk)
    return JsonResponse(list(questions.values()), safe=False)


@login_required
def get_answers(request):
    print(request.body)
    question_pk = json.loads(request.body).get('question_pk')
    answers = Answer.objects.filter(question=question_pk)
    return JsonResponse(list(answers.values()), safe=False)


@login_required
def ajax(request):

    player, created = Player.objects.get_or_create(player=request.user)

    categories = Category.objects.all()
    questions = Question.objects.all()
    answers = Answer.objects.all()

    form = AjaxForm(request.POST or None)

    if form.is_valid():
        print("Form is valid")
        question = get_object_or_404(Question, pk=request.POST.get('question_pk'))
        answer = get_object_or_404(Answer, pk=request.POST.get('answer_pk'))
        player.questions_answered.add(question)
        if answer == question.correct_answer:
            player.score = player.score + 1
            player.save()
        return redirect('ajax:ajax')

    context = {
        'player': player,
        'categories': categories,
        'questions': questions,
        'answers': answers,
        'form': form,
    }

    return render (request, 'ajax/ajax.html', context)
