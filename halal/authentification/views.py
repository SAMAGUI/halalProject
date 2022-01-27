from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from authentification.decorators import unauthenticated_user

# Create your views here.
from .forms import CreateUserForm
from django.contrib import messages

# le décorateur @unauthenticated_user permet d'interdir aux users l'accès à la page de login et d'inscription via l'url après authentification


# @unauthenticated_user
def registerPage(request):
	form = CreateUserForm(request.POST)
	if form.is_valid():
		form.save()
		user = form.cleaned_data.get('username')
		messages.success(request, 'Compte',user ,'créé avec succès')
		return redirect('login') 
	context = {'form': form}
	return render(request, 'auth/register.html', context)



# @unauthenticated_user
def loginPage(request):	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'auth/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def index(request):
    return render(request, 'user_page.html')