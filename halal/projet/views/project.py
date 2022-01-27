from projet.models import Projet
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, resolve

from projet.forms import ProjetForm

def projet_list(request):
    selected = "projets"
    projets = Projet.objects.all()   
    context ={
        'projets': projets,
    }
        
    return render(request, 'projet/projet_list.html', context)


def projet_create(request):
    form = ProjetForm
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return reverse_lazy('projet_list')
        
    context = {'form': form}
    return render(request, 'projet/projet_create.html', context)
        


class CreateProjet(CreateView):
    model = Projet
    form_class = ProjetForm
    template_name = "projet/projet_create.html"
    
    def get_success_url(self):
        return reverse_lazy("projet_detail", kwargs={'pk': self.object.id})

class UpdateProjet(UpdateView):
    model = Projet
    form_class = ProjetForm
    template_name = "projet/projet_create.html"
    
    def get_success_url(self):
        return reverse_lazy("projet_detail", kwargs={'pk': self.object.id})

    