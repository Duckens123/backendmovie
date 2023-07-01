from django.contrib import admin

from .models import Acteur, Film, Realisateur, Avis

admin.site.register(Acteur)
admin.site.register(Realisateur)
admin.site.register(Avis)
admin.site.register(Film)
