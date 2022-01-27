from django.shortcuts import render, get_object_or_404
from projet.models import Annee_exec
from projet.forms import AnneeForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def annee_list(request):
    annees = Annee_exec.objects.all()
    context = {
        'annees': annees,
    }
    return render(request, 'annee/annee_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            annees = Annee_exec.objects.all()
            data['annee_list'] = render_to_string('annee/annee_list_2.html', {'annees': annees})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def annee_create(request):
    if request.method == 'POST':
        form = AnneeForm(request.POST)
    else:
        form = AnneeForm()
    return save_all(request, form, 'annee/annee_create.html')


def annee_update(request, id):
    annee = get_object_or_404(Annee_exec, id=id)
    if request.method == 'POST':
        form = AnneeForm(request.POST, instance=annee)
    else:
        form = AnneeForm(instance=annee)
    return save_all(request, form, 'annee/annee_update.html')


def annee_delete(request, id):
    data = dict()
    annee = get_object_or_404(Annee_exec, id=id)
    if request.method == "POST":
        annee.delete()
        data['form_is_valid'] = True
        annees = Annee_exec.objects.all()
        data['annee_list'] = render_to_string(
            'annee/annee_list_2.html', {'annees': annees})
    else:
        context = {'annee': annee}
        data['html_form'] = render_to_string(
            'annee/annee_delete.html', context, request=request)

    return JsonResponse(data)
