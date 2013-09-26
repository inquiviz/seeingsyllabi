from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
import datetime

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

def hello(request):
    return HttpResponse("Hello world")

def bacon(request):
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


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'ivi.html', {
        'form': form,
    })



def current_datetime(request):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    input = forms.TextInput(attrs={'size': 10})
    author = input.render('input', 'Name')
    title = input.render('input', 'Book title')
    edition = input.render('input', 'Edition')
    publisher = input.render('input', 'Publisher name')
    year = input.render('input', 'year')
    t = get_template('testSite.html')
    html = t.render(Context({'author': author, 'title': title, 'edition': edition, 'publisher': publisher, 'year': year}))
    return HttpResponse(html)


