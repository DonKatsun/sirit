from django.urls import path
from .views.conmutadores_views import (
    conmutadores_list, conmutador_detail,
    conmutador_create, conmutador_update,
    conmutador_delete
)

urlpatterns = [
    path('conmutador', conmutadores_list, name='conmutadores_list'),
    path('conmutador/<int:pk>/', conmutador_detail, name='conmutador_detail'),
    path('conmutador/new/', conmutador_create, name='conmutador_create'),
    path('conmutador/<int:pk>/edit/', conmutador_update, name='conmutador_update'),
    path('conmutador/<int:pk>/delete/', conmutador_delete, name='conmutador_delete'),
]
