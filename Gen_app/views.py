from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.


def Random_Word(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['word'] = get_random_string(length=14)
    request.session['counter'] += 1
    return render(request, 'index.html')


def Generate(request):
    request.session['gen'] += 1
    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/Random_Word')
