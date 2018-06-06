from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm# Create your views here.
from django.contrib.auth.decorators import login_required,user_passes_test 
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
# Create your views here.
from .forms import AddArticleForm
from .models import Article
import datetime

def index(request):
     Articles = Article.objects.filter()
     return render(request, 'index.html',context={'articles':Articles})

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('index'))
    else:
        f = UserCreationForm()
    return render(request, 'signup.html', {'form': f})

@login_required
def dashboard(request):
    Articles = Article.objects.filter()
    print(Articles)
    return render(request,'list_articles.html',context={'articles':Articles})

@login_required
def writepost(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
	title = form['article_name'].value()
        if form.is_valid():
            form.save() 
	    article_date_update = Article.objects.get(owner=request.user,article_name=title)
	    article_date_update.date = 	datetime.datetime.now()	
            article_date_update.save()
        else:
            print "not valid"           
    	return HttpResponseRedirect(reverse('dashboard'))	
    args={}
    args['form'] = AddArticleForm(initial={'owner':request.user})
    return render(request,'add_post.html',args)

def readpost(request,pk):
    article = Article.objects.get(id=pk)
    return render(request,'readpost.html',context={'article':article})
