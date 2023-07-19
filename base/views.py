from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . models import Suggestion, Topic
from . forms import SuggestionForm


suggestions = [

	{"id": 1,  "name":"A Suggestion system"},
	{"id": 2,  "name":"A digital environment"},
	{"id": 3,  "name":"Technology advancement"},
	{"id": 4,  "name":"ICT is a good course"},


]


def home(request):
	q = request.GET.get('q') if request.GET.get('q') !=None else ''
	suggestion=Suggestion.objects.all()
	# suggestions=Suggestion.objects.filter(topic__name__icontains=q)
	topics = Topic.objects.all()
	context={'suggestions' : suggestions, 'topics': topics}
	return render(request, 'home.html', context=context)

def suggestion(request, pk):
	suggestion = Suggestion.objects.get(id=pk)
	# suggestion = None

	# for i in suggestions:
	# 	if i ['id']==int(pk):
	# 		suggestion = i
	
	context = {'suggestion' : suggestion }
	return render(request, 'suggestion.html', context=context)

def createSuggestion(request):
	form=SuggestionForm()

	if request.method=='POST':
		form=SuggestionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'suggestion_form.html', context)


def updateSuggestion(request, pk):
	suggestion=Suggestion.objects.get(id=pk)
	form=SuggestionForm(instance=suggestion)
	if request.method=='POST':
		form=SuggestionForm(request.POST, instance=suggestion)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form': form}

	return render(request, 'suggestion_form.html', context)


def deleteSuggestion(request, pk):
	suggestion=Suggestion.objects.get(id=pk)

	if request.method=='POST':
		suggestion.delete()
		return redirect('home')
	return render(request, 'delete.html', {'obj': suggestion})



def login_view(request):
	if request.method=='POST':
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is None:
			context = {"Error": "Invalid Username or Password"}
			return render(request, 'login.html', context)
		login(request, user)
		return redirect('/')

	return render(request, 'login.html', {})

def logout_view(request):
	return render(request, 'logout.html')



def about(request):
	return render(request, 'about.html')





