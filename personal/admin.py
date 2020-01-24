from django.contrib import admin

# Register your models here.
from personal.models import PersonaModel
@admin.register(PersonaModel)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'edad' ,'direccion' ,)
