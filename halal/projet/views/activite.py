from django.shortcuts import render, get_object_or_404
from projet.models import Activite
from projet.forms import ActiviteForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def activite_list(request):
    activites = Activite.objects.all()
    context = {
        'activites': activites,
    }
    return render(request, 'activite/activite_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            activites = Activite.objects.all()
            data['activite_list'] = render_to_string('activite/activite_list_2.html', {'activites': activites})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def activite_create(request):
    if request.method == 'POST':
        form = ActiviteForm(request.POST)
    else:
        form = ActiviteForm()
    return save_all(request, form, 'activite/activite_create.html')


def activite_update(request, id):
    activite = get_object_or_404(Activite, id=id)
    if request.method == 'POST':
        form = ActiviteForm(request.POST, instance=activite)
    else:
        form = ActiviteForm(instance=activite)
    return save_all(request, form, 'activite/activite_update.html')


def activite_delete(request, id):
    data = dict()
    activite = get_object_or_404(Activite, id=id)
    if request.method == "POST":
        activite.delete()
        data['form_is_valid'] = True
        activites = Activite.objects.all()
        data['activite_list'] = render_to_string(
            'activite/activite_list_2.html', {'activites': activites})
    else:
        context = {'activite': activite}
        data['html_form'] = render_to_string(
            'activite/activite_delete.html', context, request=request)

    return JsonResponse(data)
