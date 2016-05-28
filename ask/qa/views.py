from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, Http404
from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'qa/question_details.html', {
        'question': question,
        'answers': question.answer_set.all()
    })


def question_list(request):
    if request.path.endswith('popular/'):
        questions = Question.objects.order_by('-rating')
    else:
        questions = Question.objects.order_by('-added_at')
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/question_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })
