from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Question, Answer
from .forms import AskForm, AnswerForm, LoginForm, SignupForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question_details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = AnswerForm(initial={'question': question_id})
    if request.method == 'GET':
        return render(request, 'qa/question_details.html', {
            'question': question,
            'answers': question.answer_set.all(),
            'form': form,
        })
    elif request.method == 'POST':
        return add_answer(request)


def add_answer(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    elif request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question_id = form.cleaned_data['question']
            question = Question.objects.get(id=question_id)
            answer = Answer(
                text=form.cleaned_data['text'],
                question=question,
            )
            question.answer_set.add(answer)
            question.save()
            url = '/question/' + str(question_id)
            return HttpResponseRedirect(url)


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


def question_add(request):
    if request.method == 'GET':
        return render(request, 'qa/question_add.html', {
            'form': AskForm,
        })
    elif request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.save()
            url = '/question/' + str(question.id)
            return HttpResponseRedirect(url)


def login_user(request):
    if request.method == 'GET':
        return render(request, 'qa/login.html', {
            'form': LoginForm,
        })
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'qa/login.html', {'form': form})


def signup(request):
    if request.method == 'GET':
        return render(request, 'qa/signup.html', {
            'form': SignupForm,
        })
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'])
            user.save()
            return login_user(request)


