from django import forms

from .models import Instagram

class InstagramForms(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = [
            'nama_depan',
            'nama_belakang',
            'username'
        ]