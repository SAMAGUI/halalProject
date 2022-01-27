from django.shortcuts import render, get_object_or_404
from projet.models import Departement
from projet.forms import DepartementForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def departement_list(request):
    departements = Departement.objects.all().order_by('designation')
    context = {
        'departements': departements,
    }
    return render(request, 'departement/departement_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            departements = Departement.objects.all()
            data['departement_list'] = render_to_string('departement/departement_list_2.html', {'departements': departements})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def departement_create(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
    else:
        form = DepartementForm()
    return save_all(request,form,'departement/departement_create.html')


def departement_update(request, id):
    departement = get_object_or_404(Departement, id=id)
    if request.method == 'POST':
        form = DepartementForm(request.POST, instance=departement)
    else:
        form = DepartementForm(instance=departement)
    return save_all(request, form, 'departement/departement_update.html')


def departement_delete(request, id):
    data = dict()
    departement = get_object_or_404(Departement, id=id)
    if request.method == "POST":
        departement.delete()
        data['form_is_valid'] = True
        departements = Departement.objects.all()
        data['departement_list'] = render_to_string(
            'departement/departement_list_2.html', {'departements': departements})
    else:
        context = {'departement': departement}
        data['html_form'] = render_to_string(
            'departement/departement_delete.html', context, request=request)

    return JsonResponse(data)
