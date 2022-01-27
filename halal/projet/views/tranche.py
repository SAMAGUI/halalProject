from django.shortcuts import render, get_object_or_404
from projet.models import Tranche
from projet.forms import TrancheForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def tranche_list(request):
    tranches = Tranche.objects.all()
    context = {
        'tranches': tranches,
    }
    return render(request, 'tranche/tranche_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tranches = Tranche.objects.all()
            data['tranche_list'] = render_to_string('tranche/tranche_list_2.html', {'tranches': tranches})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def tranche_create(request):
    if request.method == 'POST':
        form = TrancheForm(request.POST)
    else:
        form = TrancheForm()
    return save_all(request, form, 'tranche/tranche_create.html')


def tranche_update(request, id):
    tranche = get_object_or_404(Tranche, id=id)
    if request.method == 'POST':
        form = TrancheForm(request.POST, instance=tranche)
    else:
        form = TrancheForm(instance=tranche)
    return save_all(request, form, 'tranche/tranche_update.html')


def tranche_delete(request, id):
    data = dict()
    tranche = get_object_or_404(Tranche, id=id)
    if request.method == "POST":
        tranche.delete()
        data['form_is_valid'] = True
        tranches = Tranche.objects.all()
        data['tranche_list'] = render_to_string(
            'tranche/tranche_list_2.html', {'tranches': tranches})
    else:
        context = {'tranche': tranche}
        data['html_form'] = render_to_string(
            'tranche/tranche_delete.html', context, request=request)

    return JsonResponse(data)
