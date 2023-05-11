from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import url, include
from adminlte3_theme.views import preguntasAdmin
urlpatterns = [
    path('preguntas/admin',preguntasAdmin , name="preguntas" ),

]
