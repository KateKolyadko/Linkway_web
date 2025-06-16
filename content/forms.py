from django import forms
from .models import NewsRegistration
import re

class NewsRegistrationForm(forms.ModelForm):
    class Meta:
        model = NewsRegistration
        fields = [
            'company_name', 
            'email', 
            'phone', 
            'first_name', 
            'last_name', 
            'position'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+375 (XX) XXX-XX-XX'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'company_name': 'Компания',
            'email': 'Email',
            'phone': 'Телефон',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'position': 'Должность',
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Упрощенная валидация телефонного номера
            if not re.match(r'^\+?[0-9\s\-\(\)]{7,20}$', phone):
                raise forms.ValidationError('Введите корректный номер телефона')
        return phone