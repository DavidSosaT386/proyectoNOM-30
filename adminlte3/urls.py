from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import url, include

from adminlte3.views import home,registro, almacen,oficina, subestacion, Anexos, coverletter_export




from adminlte3.views import home,registro, almacen,oficina, subestacion, Anexos, change, cambiarPerfil


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
     path('change/', change, name="change" ),
      path('changeProfile/', cambiarPerfil, name="changeProfile" ),
   
    path('', home, name="index" ),
    path('almacen/<alma>',almacen , name="almacen" ),
    path('registro/',registro , name="registro" ),
     path('oficina/<off>',oficina , name="oficina" ),
     path('subestacion/<sub>',subestacion , name="subestacion" ),

     path('anexos/<n_reporte>',Anexos , name="anexos" ),
     
     path('coverletter/export/<establis>/<no_reporte>', coverletter_export, name='coverletter_export'), 
     
      


     path('anexos/<n_reporte>/<establis>',Anexos , name="anexos" ),

    
]


