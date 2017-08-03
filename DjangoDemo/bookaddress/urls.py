from django.conf.urls import url
from bookaddress import views

# Importante el orden en el cual agregamos las urls. Django busca en orden alguna que haga match con la url
# ingresada, la primera que encuentra es la que toma control de la aplicación.
# https://docs.djangoproject.com/en/1.11/topics/http/urls/
urlpatterns = [
    url(r'my_data/$', views.my_data, name='my_data'),
    url(r'login/$', views.login_view, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'$', views.index),
]
