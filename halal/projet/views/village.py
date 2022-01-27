# from dal import autocomplete
from django.shortcuts import render, get_object_or_404
from projet.models import Commune, Village
from projet.forms import VillageForm, Village_Form
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required



def village_list(request):
    villages = Village.objects.all()
    context = {
        'villages': villages,
    }
    return render(request, 'village/village_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            villages = Village.objects.all()
            data['village_list'] = render_to_string('village/village_list_2.html', {'villages': villages})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def village_create(request):
    if request.method == 'POST':
        form = VillageForm(request.POST)
    else:
        form = VillageForm()
    return save_all(request, form, 'village/village_create.html')

def add_village(request):
    if request.method == 'POST':
        form = Village_Form(request.POST)
    else:
        form = Village_Form()
    return save_all(request, form, 'village/add_village.html')

def communes(request):
    form = Village_Form(request.GET)    
    return HttpResponse(form['commune'])


def create_village(request):
    form = Village_Form()
    context = {
        'form': form,
    }
    return render(request,'village/new_village.html', context)


def village_update(request, id):
    village = get_object_or_404(Village, id=id)
    if request.method == 'POST':
        form = VillageForm(request.POST, instance=village)
    else:
        form = VillageForm(instance=village)
    return save_all(request, form, 'village/village_update.html')


def village_delete(request, id):
    data = dict()
    village = get_object_or_404(Village, id=id)
    if request.method == "POST":
        village.delete()
        data['form_is_valid'] = True
        villages = Village.objects.all()
        data['village_list'] = render_to_string(
            'village/village_list_2.html', {'villages': villages})
    else:
        context = {'village': village}
        data['html_form'] = render_to_string(
            'village/village_delete.html', context, request=request)

    return JsonResponse(data)

def load_communes(request):
    departement_id = request.GET.get('departement')
    communes = Commune.objects.filter(departement_id=departement_id).order_by('designation')
    return render(request, 'village/communes_dropdown_list_options.html', {'communes': communes})


# class VillageAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         # Don't forget to filter out results depending on the visitor !
#         # if not self.request.user.is_authenticated:
#         #     return Village.objects.none()

#         qs = Village.objects.all()

#         if self.q:
#             qs = qs.filter(name__istartswith=self.q)

#         return qs
        
