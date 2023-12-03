from django.contrib import admin
from .models import Medico
from .models import Departamento
from .models import Sucursal
from .models import Ambulancia

# Register your models here.
admin.site.register(Medico)

admin.site.register(Departamento)

admin.site.register(Sucursal)

admin.site.register(Ambulancia)

