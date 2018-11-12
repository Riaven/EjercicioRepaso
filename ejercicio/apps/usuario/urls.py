from django.conf.urls import url, include
from apps.usuario.views import index, user_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^userlist/', user_list, name='user_listar'),
]

