from django import forms
from .models import ProjectProposal
from content.models import Vendor

class ProjectProposalForm(forms.ModelForm):
    class Meta:
        model = ProjectProposal
        fields = '__all__'
        widgets = {
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].required = False
        self.fields['vendor'].queryset = Vendor.objects.all().order_by('name')

    def clean_attachment(self):
        file = self.cleaned_data.get('attachment')
        if file:
            if file.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Максимальный размер файла - 5 МБ")
        return file