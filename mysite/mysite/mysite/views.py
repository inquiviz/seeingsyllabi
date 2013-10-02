from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from pymongo import MongoClient
from reportlab.pdfgen import canvas
import pymongo
from pyPdf import PdfFileWriter, PdfFileReader
import datetime
fileName = ""
def display(request):
    print fileName
    return render(request, 'testSite1.html', {"fileName": fileName}) #after you click the link, it opens the text file
    

def contact(request):
    global fileName
    client = MongoClient('localhost', 27017)
    db = client.test
    posts = db.posts				#make sure when you upload to mongo it is in DB "test" and collection "posts"
    print db.collection_names()
    pdf_file = False 				#this is to make a link appear if something is found
    file = open('stuff4.txt', 'w+')		#open stuff4.txt (will be empty likely)
    if request.method == 'POST': # If the form has been submitted...
        post_temp = request.POST.copy()           # creates a copy of the .POST data
        value = post_temp['author']
        post_temp['author'] = ''                    #clears title
        hello = posts.find_one({"author": value})
        if hello != None:				#if you get something back from mongo, execute
		fileName = 'stuff4.txt'			#set the name to stuff4.txt
        	file.write(hello['contents'])		#write to it
		pdf_file = True

	form = ContactForm(post_temp)
        if form.is_valid(): # All validation rules pass    
            
            # Process the data in form.cleaned_data
            # ...
            return render(request, 'ivi.html', {
                'form': form.as_p, 'file': 'stuff.txt', 'pdf_file': pdf_file,
  	    })
    else:
        form = ContactForm() # An unbound form
    return render(request, 'ivi.html', {
        'form': form.as_p,
    })


class ContactForm(forms.Form):
    CHOICES = (('1', 'First',), ('2', 'Second',), ('3', 'Third',), ('4', 'Fourth',))
    author = forms.CharField(max_length=100, required=False, label = '  Author')
    title = forms.CharField(required=False, label = '    Title')
    edition = forms.CharField(required=False, label = '  Edition')
    publisher = forms.CharField(required=False, label = 'Publisher')
    year = forms.CharField(required=False, label = 'Title') 
    english = forms.BooleanField(required=False)
    biology = forms.BooleanField(required=False)
    history = forms.BooleanField(required=False)
    computer_science = forms.BooleanField(required=False)
    education = forms.BooleanField(required=False)
    options = forms.ChoiceField(choices = CHOICES)


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
    t = get_template('testSite.html')
    html = t.render(Context({'author': author, 'title': title, 'edition': edition, 'publisher': publisher, 'year': year}))
    return HttpResponse(html)


