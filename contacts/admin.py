from django.contrib import admin
from .models import PartnershipRequest

@admin.register(PartnershipRequest)
class PartnershipRequestAdmin(admin.ModelAdmin):
    list_display = ('partner_name', 'email', 'source', 'created_at', 'agree_terms')
    list_filter = ('source', 'subscribe_newsletter', 'agree_terms')
    search_fields = ('partner_name', 'email', 'address')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('partner_name', 'email', 'address', 'source')
        }),
        ('Дополнительно', {
            'fields': ('comments', 'subscribe_newsletter', 'agree_terms', 'created_at')
        }),
    )
