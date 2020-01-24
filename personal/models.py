from django.db import models

# Create your models here.
class PersonaModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150 , null=True, blank=True, default=None)
    edad = models.PositiveIntegerField()
    direccion = models.CharField(max_length=150)

    class Meta:
        db_table = 'db_personal'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'



