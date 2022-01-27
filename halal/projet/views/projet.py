from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
# Create your views here.
from projet.models import *
from projet.forms import ProjetForm
from django.http import JsonResponse
from django.template.loader import render_to_string



def projet_list(request):
	projets = Projet.objects.all()

	return render(request, 'projet/projet_list.html', {'projets':projets})


def projet_delete(request, id):
    data = dict()
    projet = get_object_or_404(Projet, id=id)
    if request.method == "POST":
        projet.delete()
        data['form_is_valid'] = True
        projets = Projet.objects.all()
        data['projet_list'] = render_to_string('projet/projet_list.html', {'projets': projets})
    else:
        context = {'projet': projet}
        data['html_form'] = render_to_string('projet/projet_delete.html', context, request=request)

    return JsonResponse(data)



def projet_create(request):
	form = ProjetForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ProjetForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('projet_list')

	context = {'form':form}
	return render(request, 'projet/projet_create.html', context)
    # return render(request, 'projet/projet_create.html')



def projet_update(request, pk):

	projet = Projet.objects.get(id=pk)
	form = ProjetForm(instance=projet)

	if request.method == 'POST':
		form = ProjetForm(request.POST, request.FILES, instance=projet)
		if form.is_valid():
			form.save()
			return redirect('projet_list')

	context = {'form':form}
	return render(request, 'projet/projet_create.html', context)



def projet_detail(request, id):
	projet = Projet.objects.get(id=id)
	# if request.method == "POST":
	# 	projet.delete()
	# 	return redirect('/')

	context = {'projet':projet}
	return render(request, 'projet/projet_detail.html', context)

