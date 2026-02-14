from django.contrib import admin
from .models import OrganizationalChart, OrganizationalChartPage


@admin.register(OrganizationalChart)
class OrganizationalChartAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'level')
    list_filter = ('level',)
    search_fields = ('name', 'description')


admin.site.register(OrganizationalChartPage)
