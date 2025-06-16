from django import forms
from .models import PartnershipRequest

class PartnershipRequestForm(forms.ModelForm):
    class Meta:
        model = PartnershipRequest
        fields = [
            'partner_name', 'email', 'address', 'source',
            'comments', 'subscribe_newsletter', 'agree_terms'
        ]
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 3}),
        }
    
    agree_terms = forms.BooleanField(
        error_messages={'required': 'Вы должны принять условия'},
    )