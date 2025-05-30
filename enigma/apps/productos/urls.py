# apps/usuarios/urls.py
# from django.urls import path
# from .views import test_view

# urlpatterns = [
    # path('test/', test_view),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('nuevo/', views.crear_producto, name='crear_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
