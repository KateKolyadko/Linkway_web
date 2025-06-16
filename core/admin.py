from django.contrib import admin
from .models import ProjectProposal

@admin.register(ProjectProposal)
class ProjectProposalAdmin(admin.ModelAdmin):
    list_display = ('partner_name', 'customer_name', 'vendor', 'created_at')
    list_filter = ('vendor', 'created_at')
    search_fields = ('partner_name', 'customer_name', 'email')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('partner_name', 'email', 'customer_name', 'vendor')
        }),
        ('Дополнительно', {
            'fields': ('comments', 'attachment', 'created_at')
        }),
    )