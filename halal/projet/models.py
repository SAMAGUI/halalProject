from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.



class Type_projet(models.Model):
    designation = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.designation}"
    
    
class Departement(models.Model):
    designation = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.designation}"
        
    
    
class Tranche(models.Model):
    designation = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.designation}"
    
class Commune(models.Model):
    designation = models.CharField(max_length=150)
    departement = models.ForeignKey(Departement, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.designation}"
    
    def get_departement(self):
        return f"{self.departement}"
    
    
    
class Village(models.Model):
    designation = models.CharField(max_length=150)
    # departement = models.ForeignKey(Departement, blank=True, null=True, on_delete=models.SET_NULL)
    commune = models.ForeignKey(Commune, on_delete=CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.designation}"
    
    
class Annee_exec(models.Model):
    hegirien = models.CharField(max_length=150)
    gregorien = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.hegirien} - {self.gregorien}"
    
    def get_annee(self):
        return f"{self.hegirien} - {self.gregorien}"
    
    
    
class Partenaire(models.Model):
    nom = models.CharField(max_length=200)
    pays = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nom}"
    
    
    
    
class Entreprise(models.Model):
    sigle = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=150)
    raison_sociale = models.CharField(max_length=200)
    tel = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(max_length=50)
    adresse = models.CharField(max_length=150)
    responsable = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nom}"
    
class Documents_entreprise(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    fichier = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Projet(models.Model):
    numero = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    debut = models.DateField(verbose_name="Date début")
    fin = models.DateField(verbose_name="Date fin")
    budget_global = models.IntegerField()
    doc_projet = models.FileField(upload_to='', verbose_name='Document projet')
    numero_decret = models.CharField(max_length=150)
    montant_alloue = models.IntegerField(verbose_name='Montant alloué')
    partenaire = models.ForeignKey(Partenaire, on_delete=CASCADE, verbose_name='Financé par')
    type_projet = models.ForeignKey(Type_projet, on_delete=CASCADE)
    execut = models.ForeignKey(Annee_exec, on_delete=CASCADE, verbose_name="Année d'exécution")
    entreprise = models.ForeignKey(Entreprise, on_delete=CASCADE)
    village = models.ForeignKey(Village, on_delete=CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Activite(models.Model):
    designation = models.CharField(max_length=150)
    projet = models.ForeignKey(Projet, on_delete=CASCADE)
    executer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    