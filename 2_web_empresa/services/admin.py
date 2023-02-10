from django.contrib import admin
from .models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    fieldsets = (
        ('Información del servicio',
         {"fields": ('title', 'subtitle', 'content', 'image'), }),
        ('Fechas de control', {'fields': ('created', 'updated')})
    )


admin.site.register(Service, ServiceAdmin)
