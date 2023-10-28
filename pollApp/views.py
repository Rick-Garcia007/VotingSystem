from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from .models import Question, Choice

# Receba perguntas e exiba-as
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls / index.html', context)

# Mostrar perguntas e escolhas
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('A pergunta não existe')
    return render(request, 'polls / detail.html', {'question': question})

# Obtenha perguntas e exiba resultados
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls / results.html', {'question': question})

# Vote em uma escolha de pergunta
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls / detail.html', {'question': question, 'error_message': 'Você não selecionou uma opção.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args= (question.id)))