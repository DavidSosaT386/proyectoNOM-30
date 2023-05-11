from django.contrib import admin
from .models import encuesta, respuesta,anexos,porfile
# Register your models here.

class empleados(admin.ModelAdmin):
    list_display= ['clasificacion', 'sub_clasificacion', 'categoria', 'pregunta','no_pregunta',]
    list_filter= ['categoria']
    list_editable=['no_pregunta','pregunta']

admin.site.register(encuesta, empleados)
# admin.site.register(respuesta)
#admin.site.register(anexos)
admin.site.register(porfile)
