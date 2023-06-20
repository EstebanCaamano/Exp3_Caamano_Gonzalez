from django.urls import path
from .views import inicio,pagina2,formulario,api,registrar,crear,eliminar,modificar,tienda
urlpatterns=[ 
    path('', inicio, name="inicio"),
    path('pagina2/', pagina2, name="pagina2"),
    path('formulario/',formulario , name="formulario"),
    path('api/',api , name="api"),
    path('registrar/',registrar,name="registrar"),
    path('crear/',crear,name="crear"),
    path('modificar/<idproducto>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar, name="eliminar"),
    path('pagina3/',tienda,name="pagina3"),
    

]


