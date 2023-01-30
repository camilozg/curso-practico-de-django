from django.contrib import admin
from . import models

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    fieldsets = [
        ('Información principal', {
         'fields': ['title', 'description', 'image']}),
        ('Información opcional', {'fields': ['link']}),
        ('Fechas de control', {'fields': ['created', 'updated']})
    ]


admin.site.register(models.Project, ProjectAdmin)
