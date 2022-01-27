from django.shortcuts import render, get_object_or_404
from projet.models import Commune
from projet.forms import CommuneForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def commune_list(request):
    communes = Commune.objects.all()
    context = {
        'communes': communes,
    }
    return render(request, 'commune/commune_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            communes = Commune.objects.all()
            data['commune_list'] = render_to_string('commune/commune_list_2.html', {'communes': communes})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def commune_create(request):
    if request.method == 'POST':
        form = CommuneForm(request.POST)
    else:
        form = CommuneForm()
    return save_all(request, form, 'commune/commune_create.html')


def commune_update(request, id):
    commune = get_object_or_404(Commune, id=id)
    if request.method == 'POST':
        form = CommuneForm(request.POST, instance=commune)
    else:
        form = CommuneForm(instance=commune)
    return save_all(request, form, 'commune/commune_update.html')


def commune_delete(request, id):
    data = dict()
    commune = get_object_or_404(Commune, id=id)
    if request.method == "POST":
        commune.delete()
        data['form_is_valid'] = True
        communes = Commune.objects.all()
        data['commune_list'] = render_to_string(
            'commune/commune_list_2.html', {'communes': communes})
    else:
        context = {'commune': commune}
        data['html_form'] = render_to_string(
            'commune/commune_delete.html', context, request=request)

    return JsonResponse(data)
