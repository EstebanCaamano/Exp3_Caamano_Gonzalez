from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=3, verbose_name="Identificador")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    imagen = models.ImageField(upload_to="imagenes",null=True,verbose_name="Imagen")
    precio = models.CharField(max_length=15, blank=True ,verbose_name="Precio")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    
    def __str__(self):
        return self.id +' '+self.nombre

