from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
from django import forms
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    input = forms.TextInput(attrs={'size': 10})
    author = input.render('input', 'Name')
    title = input.render('input', 'Book title')
    edition = input.render('input', 'Edition')
    publisher = input.render('input', 'Publisher name')
    year = input.render('input', 'year')
    t = get_template('ivi.html')
    html = t.render(Context({'author': author, 'title': title, 'edition': edition, 'publisher': publisher, 'year': year}))
    return HttpResponse(html)