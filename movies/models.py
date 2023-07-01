from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Realisateur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    pays_origine = models.CharField(max_length=100)
    biographie = models.TextField()

    def __str__(self):
        return self.nom+ ' '+ self.prenom


class Acteur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    pays_origine = models.CharField(max_length=100)
    biographie = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom+ ' '+ self.prenom

class Film(models.Model):
    titre = models.CharField(max_length=255)
    realisateur = models.ManyToManyField(Realisateur)
    acteurs = models.ManyToManyField(Acteur)
    synopsis = models.TextField()
    genre = models.CharField(max_length=100)
    annee_sortie = models.IntegerField()
    duree = models.IntegerField()
    iframe = models.TextField(default='<IFRAME SRC="https://uqload.co/embed-xxe5frf09hqv.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=640 HEIGHT=360 allowfullscreen></IFRAME>')
    image = CloudinaryField('image', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    imagecaptions = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.titre

class Avis(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField(null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)