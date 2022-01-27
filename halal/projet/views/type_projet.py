from django.shortcuts import render, get_object_or_404
from projet.models import Type_projet
from projet.forms import TypeForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def type_list(request):
    types = Type_projet.objects.all()
    context = {
        'types': types,
    }
    return render(request, 'type/type_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            types = Type_projet.objects.all()
            data['type_list'] = render_to_string('type/type_list_2.html', {'types': types})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def type_create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
    else:
        form = TypeForm()
    return save_all(request, form, 'type/type_create.html')


def type_update(request, id):
    type = get_object_or_404(Type_projet, id=id)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
    else:
        form = TypeForm(instance=type)
    return save_all(request, form, 'type/type_update.html')


def type_delete(request, id):
    data = dict()
    type = get_object_or_404(Type_projet, id=id)
    if request.method == "POST":
        type.delete()
        data['form_is_valid'] = True
        types = Type_projet.objects.all()
        data['type_list'] = render_to_string(
            'type/type_list_2.html', {'types': types})
    else:
        context = {'type': type}
        data['html_form'] = render_to_string(
            'type/type_delete.html', context, request=request)

    return JsonResponse(data)
