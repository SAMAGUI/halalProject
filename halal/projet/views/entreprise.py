from django.shortcuts import redirect, render, get_object_or_404
from projet.models import Entreprise
from projet.forms import EntrepriseForm, DocEntrepriseForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf



def entreprise_list(request):
    entreprises = Entreprise.objects.all()
    context = {
        'entreprises': entreprises,
    }
    return render(request, 'entreprise/entreprise_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            entreprises = Entreprise.objects.all()
            data['entreprise_list'] = render_to_string('entreprise/entreprise_list_2.html', {'entreprises': entreprises})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



def all_save(request, form1, form2, template_name):
    data = dict()
    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid():
            entrep = form1.save()
            docum = form2.save(False)
            docum.entreprise = entrep
            docum.save()
            data['form_is_valid'] = True
            entreprises = Entreprise.objects.all()
            data['entreprise_list'] = render_to_string('entreprise/entreprise_list_2.html', {'entreprises': entreprises})
        else:
            data['form_is_valid'] = False
    context = {
        'form1': form1,
        'form2': form2,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def create_entreprise(request):
    if request.method == 'POST':
        form_entreprise = EntrepriseForm(request.POST)
        form_document = DocEntrepriseForm(request.POST, request.FILES)
    else:
        form_entreprise = EntrepriseForm()
        form_document = DocEntrepriseForm()
    return all_save(request, form_entreprise, form_document, 'entreprise/create_entreprise.html')



def entreprise_create(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
    else:
        form = EntrepriseForm()
    return save_all(request, form, 'entreprise/entreprise_create.html')


def entreprise_update(request, id):
    entreprise = get_object_or_404(Entreprise, id=id)
    if request.method == 'POST':
        form = EntrepriseForm(request.POST, instance=entreprise)
    else:
        form = EntrepriseForm(instance=entreprise)
    return save_all(request, form, 'entreprise/entreprise_update.html')


def entreprise_delete(request, id):
    data = dict()
    entreprise = get_object_or_404(Entreprise, id=id)
    if request.method == "POST":
        entreprise.delete()
        data['form_is_valid'] = True
        entreprises = Entreprise.objects.all()
        data['entreprise_list'] = render_to_string(
            'entreprise/entreprise_list_2.html', {'entreprises': entreprises})
    else:
        context = {'entreprise': entreprise}
        data['html_form'] = render_to_string(
            'entreprise/entreprise_delete.html', context, request=request)

    return JsonResponse(data)

def new_entreprise(request):
    if request.method == 'POST':
        form_ent = EntrepriseForm(request.POST)
        form_doc = DocEntrepriseForm(request.POST, request.FILES)
        
        if form_ent.is_valid() and form_doc.is_valid():            
            entreprise = form_ent.save()
            doc = form_doc.save(False)
            
            doc.entreprise = entreprise
            doc.save()
            return redirect('entreprise_list')
    else:
        form_ent = EntrepriseForm()
        form_doc = DocEntrepriseForm()
    args = {}
    args.update(csrf(request))
    args['form_ent'] = form_ent
    args['form_doc'] = form_doc    
    return render(request, 'entreprise/new_entreprise.html', args)
        
# def new_vente(request):
#     if request.method == 'POST':
#         vente_form = EntrepriseForm(request.POST)
#         detail_form = DocEntrepriseForm(request.POST, request.FILES)
        
#         if vente_form.is_valid() and detail_form.is_valid():
#             vente = vente_form.save()
#             detail = detail_form.save(False)
            
#             detail.vente=vente
#             # detail.saisie_par=request.user
#             detail.save()
            
#             return redirect('vente')
#     else:
#         vente_form = VenteForm()
#         detail_form = DocEntrepriseForm()
#     args = {}
#     args.update(csrf(request))
#     args['vente_form'] = vente_form
#     args['detail_form'] = detail_form
    
#     return render(request, 'ventes/create.html', args)
