from django.contrib import admin
from .models import Usuario, Equipo, Arriendo
# Register your models here.


admin.site.register([Usuario, Equipo, Arriendo])