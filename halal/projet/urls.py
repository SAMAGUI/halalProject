from re import template
from django.urls import path
from django.views.generic.detail import DetailView
from projet.views import  annee, departement, type_projet, commune, village, partenaire, tranche, entreprise, projet
from projet import viewsd
from projet.models import Projet

urlpatterns = [
    
    path('', viewsd.index, name='home'),
    
    path('annees', annee.annee_list, name='annee_list'),
    path('annees/create/', annee.annee_create, name='annee_create'),
    path('annees/<str:id>/update/', annee.annee_update, name='annee_update'),
    path('annees/<str:id>/delete/', annee.annee_delete, name='annee_delete'), 
    
    
    path('departements', departement.departement_list, name='departement_list'),
    path('departements/create/', departement.departement_create, name='departement_create'),
    path('departements/<str:id>/update/', departement.departement_update, name='departement_update'),
    path('departements/<str:id>/delete/', departement.departement_delete, name='departement_delete'), 
    
    
    
    path('types', type_projet.type_list, name='type_list'),
    path('types/create/', type_projet.type_create, name='type_create'),
    path('types/<str:id>/update/', type_projet.type_update, name='type_update'),
    path('types/<str:id>/delete/', type_projet.type_delete, name='type_delete'),
    
    path('communes', commune.commune_list, name='commune_list'),
    path('communes/create/', commune.commune_create, name='commune_create'),
    path('communes/<str:id>/update/', commune.commune_update, name='commune_update'),
    path('communes/<str:id>/delete/', commune.commune_delete, name='commune_delete'), 
    
    
    path('villages', village.village_list, name='village_list'),
    path('villages/create/', village.village_create, name='village_create'),
    path('villages/<str:id>/update/', village.village_update, name='village_update'),
    path('villages/<str:id>/delete/', village.village_delete, name='village_delete'),
    path('ajax/load-communes/', village.load_communes, name='ajax_load_communes'),
    # path('village-autocomplete', village.Village_autocomplete.as_view(), name='village_autocomplete'),
    path('villages/new/', village.create_village, name='village_new'),
    path('villages/add/', village.add_village, name='add_village'),
    path('communes/', village.communes, name='communes'),
    
    
    path('partenaires', partenaire.partenaire_list, name='partenaire_list'),
    path('partenaires/create/', partenaire.partenaire_create, name='partenaire_create'),
    path('partenaires/<str:id>/update/', partenaire.partenaire_update, name='partenaire_update'),
    path('partenaires/<str:id>/delete/', partenaire.partenaire_delete, name='partenaire_delete'),
    
    
    path('tranches', tranche.tranche_list, name='tranche_list'),
    path('tranches/create/', tranche.tranche_create, name='tranche_create'),
    path('tranches/<str:id>/update/', tranche.tranche_update, name='tranche_update'),
    path('tranches/<str:id>/delete/', tranche.tranche_delete, name='tranche_delete'),  
    
    
    path('entreprises', entreprise.entreprise_list, name='entreprise_list'),
    path('entreprises/create/', entreprise.entreprise_create, name='entreprise_create'),
    path('entreprises/new/', entreprise.new_entreprise, name='create_entreprise'),
    path('entreprises/<str:id>/update/', entreprise.entreprise_update, name='entreprise_update'),
    path('entreprises/<str:id>/delete/', entreprise.entreprise_delete, name='entreprise_delete'), 
    
    path('projets/', projet.projet_list, name="projet_list"),
    path('projets/create/', projet.projet_create, name="projet_create"),
    path('projets/update/<int:pk>/', projet.projet_update, name="projet_update"),
    path('projets/<str:id>/delete/', projet.projet_delete, name='projet_delete'),
    path('projets/<str:id>', projet.projet_detail, name='projet_detail'),
    # path('projets/<int:pk>/', DetailView.as_view(model=Projet, template_name="projet/projet_detail.html"), name="projet_detail"),

]