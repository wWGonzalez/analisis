"""myPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#from .views import vistaPrincipal,vistaEstudiante,listaEstudiante,vistaEstudianteAdministrador,listaEstudianteAdministrador,vistaArticulo,listaArticulo,vistaComentario,listaComentario,LoginView,vistaVideo
from .views import vistaPrincipal,vistaHabitacion,listaHabitacion,vistaCliente,listaCliente,LoginView,logout_view
from django.contrib.auth.views import login,logout

urlpatterns = [
	url(r'^$', vistaPrincipal.as_view()),
	url(r'^principal$', vistaPrincipal.as_view(), name = 'principal'),
    url(r'^login$', LoginView.as_view(), name = 'login'),
    url(r'^logout$', logout_view,name='logout'),

	url(r'^habitacion$', vistaHabitacion.as_view(), name = 'habitacion'),
    url(r'^listaHabitacion$', listaHabitacion.as_view(), name = 'listaHabitacion'),

    url(r'^cliente$', vistaCliente.as_view(), name = 'cliente'),
    url(r'^listaCliente$', listaCliente.as_view(), name = 'listaCliente'),

   # url(r'^accounts/logout/$', logout, name = 'logout'),
]
