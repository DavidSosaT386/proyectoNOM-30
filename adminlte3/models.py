from django.db import models
from django.conf import settings
from django.core.files import File
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

import urllib
import os
preguntas_choices = (
    ("categoria1", "Almacén"),
    ("categoria2", "Oficina"),
    ("categoria3", "Subestación"),
)

clasificacion_choices = (
    ("clas1", "Localización"),
    ("clas2", "Condiciones de la instalación"),
    ("clas3", "Riesgos inherentes a la instalación"),
    ("clas4", "Protección contra incendio"),
    ("clas5", "Peligros circundantes al centro de trabajo"),
    ("clas6", "Procedimientos administrativos"),
    ("clas7", "Requerimientos normativos en materia de seguridad"), 
)

subclas_choices = (
    ("clas1", "Terremotos"),
    ("clas2", "Clima / Riesgos naturales"),
    ("clas3", "Riesgos de terceros"),
    ("clas4", "Distribución"),
    ("clas5", "Antiguedad / Condiciones físicas"),
    ("clas6", "Orden y Limpieza"), 
    ("clas7", "Señalización"),
    ("clas8", "Seguridad y vigilancia"),
    ("clas9", "Riesgos inherentes"),
    ("clas10", "Prevención del fuego"),
    ("clas11", "Reducción del crecimiento y propagación del fuego"),
    ("clas12", "Sistema de detección y alarma de incendios"),
    ("clas13", "Sistemas fijos de extinción"),
    ("clas14", "Extintores portátiles y móviles"),  
    ("clas15", "Brigada contra incendio"),
    ("clas16", "Convenios de cooperación y ayuda mutua"),
    ("clas17", "Peligros circundantes"),
    ("clas18", "Procedimientos de mantenimiento e inspección"),
    ("clas19", "Procedimientos de seguridad"),
    ("clas20", "Protección civil / planes de emergencia / y se cuenta con los procedimientos por escrito para"),
    ("clas21", "Seguridad ambiental"),
    ("clas22", "Capacitacion y entrenamiento"),
    ("clas23", "Procedimientos para control de contratistas"),
    ("clas24", "Drenaje"), 
    ("clas25", "Procedimientos de operación"),
    ("clas26", "Caseta de control de la subestación"),
    #CLASES DE LAS SUBESTACIONES
    ("clas27", "Tableros y gabinetes de control"),
    ("clas28", "Tablero de corriente directa y corriente alterna"),
    ("clas29", "Cargadores de baterías"),
    ("clas30", "Cuarto de baterías"),
    ("clas31", "Cuarto de control supervisorio"),
    ("clas32", "Cuarto de comunicaciones"),
    ("clas33", "Transformadores, autotransformadores y reactores"),
    ("clas34", "Interruptores"),
    ("clas35", "Transformadores de instrumentos (TC´s, TP´s y DP´s)"),
    ("clas36", "Cuchillas, apartarrayos, buses y banco de capacitores"),
    ("clas37", "Trincheras y ductos de cables"),
    ("clas38", "Subestación de servicios propios"),
    ("clas39", "Predio de la subestación"),
    ("clas40", "Sistema de detección y alarma de incendio en caseta de control"),
    ("clas41", "Sistema fijo contraincendio para transformadores y autotransformadores"),
    ("clas42", "Agentes pasivos"),
    ("clas43", "Programa de trabajo de seguridad, salud y prevención de riesgos"),
)
centro_trabajo_choices = (
    ("SEDE", "SEDE"),
    ("Villahermosa", "Villahermosa"),
    ("Tuxtla gutierrez", "Tuxtla gutierrez"),
    ("Tapachula","Tapachula"),
    ("Itsmo","Itsmo"),
    ("Malpaso","Malpaso"),
    ("Zotze","Zotze"),
)
 

class encuesta(models.Model):
    id = models.AutoField(primary_key=True)
    no_pregunta= models.IntegerField(null=True)
    pregunta = models.CharField(max_length=1000)
    clasificacion =  models.CharField(max_length=280,  choices=clasificacion_choices, default="clas6")
    sub_clasificacion = models.CharField(max_length=280,  choices=subclas_choices, default="clas1")
    categoria =  models.CharField(max_length=50, choices=preguntas_choices, default="categoria1")
     
    def __str__(self):
        return str(self.no_pregunta)
    
    class Meta:
        unique_together = ('no_pregunta', 'categoria',)
        db_table = 'encuesta'
        verbose_name = 'encuesta'
        verbose_name_plural = 'encuestas'

        ordering=['no_pregunta']



class respuesta(models.Model):
    no_reporte =  models.IntegerField(null=True)
    usuario = models.ForeignKey(
      settings.AUTH_USER_MODEL, 
      on_delete=models.CASCADE, null=True
     )
    pregunta = models.ForeignKey(encuesta,on_delete=models.CASCADE)
    condicion = models.BooleanField(default = False)
    observacion  = models.TextField(null=True,blank=True)

        
    def __str__(self):
        return str(self.usuario)
    
    class Meta:
        db_table = 'respuesta'
        verbose_name = 'respuesta'
        verbose_name_plural = 'respuestas'

class anexos(models.Model):
    usuario = models.ForeignKey(
      settings.AUTH_USER_MODEL, 
      on_delete=models.CASCADE, null=True
     )
    no_reporte =  models.IntegerField(null=True)
    foto_anexo = models.ImageField(upload_to= 'images/', blank=True, null=True)
    descripcion  = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.foto_anexo)

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = anexos.objects.get(id=self.id)
        except anexos.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.foto_anexo and self.foto_anexo and obj.foto_anexo != self.foto_anexo:
            # delete the old image file from the storage in favor of the new file
            obj.foto_anexo.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.foto_anexo.delete()
        return super(anexos, self).delete(*args, **kwargs)

   
    class Meta:
        db_table = 'anexos'
        verbose_name = 'anexos'
        verbose_name_plural = 'anexos'

class porfile(models.Model):
    usuario = models.ForeignKey(
      settings.AUTH_USER_MODEL, 
      on_delete=models.CASCADE, null=True
     )
    nombre = models.CharField(max_length=100, null=True)
    apellidos = models.CharField(max_length=100, null=True)
    foto_perfil = models.ImageField(upload_to= 'perfiles/', blank=True, null=True)
    centro_trabajo = models.CharField(max_length=80  ,choices=centro_trabajo_choices, default="sede")

    def __str__(self):
        return str(self.usuario)
    
    class Meta:
        db_table = 'perfil'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfil'


