from django.shortcuts import render, get_object_or_404
from projet.models import Partenaire
from projet.forms import PartenaireForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def partenaire_list(request):
    partenaires = Partenaire.objects.all()
    context = {
        'partenaires': partenaires,
    }
    return render(request, 'partenaire/partenaire_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            partenaires = Partenaire.objects.all()
            data['partenaire_list'] = render_to_string('partenaire/partenaire_list_2.html', {'partenaires': partenaires})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def partenaire_create(request):
    if request.method == 'POST':
        form = PartenaireForm(request.POST)
    else:
        form = PartenaireForm()
    return save_all(request, form, 'partenaire/partenaire_create.html')


def partenaire_update(request, id):
    partenaire = get_object_or_404(Partenaire, id=id)
    if request.method == 'POST':
        form = PartenaireForm(request.POST, instance=partenaire)
    else:
        form = PartenaireForm(instance=partenaire)
    return save_all(request, form, 'partenaire/partenaire_update.html')


def partenaire_delete(request, id):
    data = dict()
    partenaire = get_object_or_404(Partenaire, id=id)
    if request.method == "POST":
        partenaire.delete()
        data['form_is_valid'] = True
        partenaires = Partenaire.objects.all()
        data['partenaire_list'] = render_to_string(
            'partenaire/partenaire_list_2.html', {'partenaires': partenaires})
    else:
        context = {'partenaire': partenaire}
        data['html_form'] = render_to_string(
            'partenaire/partenaire_delete.html', context, request=request)

    return JsonResponse(data)
