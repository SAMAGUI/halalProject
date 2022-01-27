from dynamic_forms import DynamicField, DynamicFormMixin
from django import forms
from projet.models import Activite, Commune, Partenaire
from projet.models import Departement, Village, Tranche, Projet
from projet.models import Annee_exec, Type_projet, Entreprise, Documents_entreprise



class AnneeForm(forms.ModelForm):
    class Meta:
        model = Annee_exec
        fields = '__all__'
        
        
        
class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'
        
class TypeForm(forms.ModelForm):
    class Meta:
        model = Type_projet
        fields = '__all__'
        
        
class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = '__all__'
        
        
        
class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = ['commune', 'designation']
    


class Village_Form(DynamicFormMixin,forms.Form):
    
    def commune_choices(form):
        departement = form['departement'].value()
        return Commune.objects.filter(departement=departement)
    
    def initial_commune(form):
        departement = form['departement'].value()
        return Commune.objects.filter(departement=departement).first()
        
    
    departement = forms.ModelChoiceField(
        queryset= Departement.objects.all(),
        initial=Departement.objects.first(),
    )
    commune = DynamicField(
        forms.ModelChoiceField,
        queryset=commune_choices,
        initial=initial_commune,
    )
    
    designation = forms.CharField()
    
        


    
        
class PartenaireForm(forms.ModelForm):
    class Meta:
        model = Partenaire
        fields = '__all__'
        
        
class TrancheForm(forms.ModelForm):
    class Meta:
        model = Tranche
        fields = '__all__'
        
        
class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__'
        
        
class DocEntrepriseForm(forms.ModelForm):
    class Meta:
        model = Documents_entreprise
        fields = '__all__'
        exclude = ['entreprise', ]


class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet;
        fields = '__all__'
        
        
    # def __init__(self, *args, **kwargs):
    #     self.fields['village'].queryset = Village.objects.none()

    #     if 'commune' in self.data:
    #         try:
    #             commune_id = int(self.data.get('commune'))
    #             self.fields['village'].queryset = Village.objects.filter(commune_id=commune_id).order_by('designation')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['village'].queryset = self.instance.commune.village_set.order_by('designation')
      
        
        # debut = forms.DateField(
        # input_formats=['%d/%m/%Y'],
        # widget=forms.DateInput(format='%d/%m/%Y' , attrs={'class': 'form-control datepicker', 'placeholder': 'Date de naissance'}), label='Date de naissance')
    
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['debut'].widget = forms.HiddenInput


class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = '__all__'
        exclude = ['executer']