
from django.shortcuts import redirect, render

from adminlte3.models import encuesta, respuesta
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def preguntasAdmin(request):
    
    if request.method == "POST":
        a= zip(
            request.POST.getlist("no_pregunta"),
            request.POST.getlist("pregunta"),
            request.POST.getlist("categoria"),
            request.POST.getlist("clasificacion"),
            request.POST.getlist("sub_clasificacion"),
            )
      
        data_dicts= [{'no_pregunta': int(no_pregunta) , 'pregunta': pregunta, 'categoria': categoria, 'clasificacion': clasi , 'sub_clasificacion': subclasi } for no_pregunta, pregunta,categoria,clasi,subclasi in a]
        for data in data_dicts:
            guard= encuesta(no_pregunta = data['no_pregunta'], pregunta = data['pregunta'], categoria= data['categoria'], clasificacion=data['clasificacion'] ,sub_clasificacion=data['sub_clasificacion'])
            guard.save()
                 
        messages.success(request,"las preguntas se han subido")
        return redirect(preguntasAdmin)
    else: 
       contexto={
           'range': range(10)
       } 
    return render(request, 'admin/preguntas.html', contexto)

