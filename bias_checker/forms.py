from django.forms import ModelForm, ValidationError
from .models import File
from django import forms
from django.core.validators import FileExtensionValidator

class FileForm(ModelForm):
    file = forms.FileField(
        widget=forms.FileInput(attrs={
            'style': '''
                background-color: #dddddd;
                color: white;
                padding: 0.5rem;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                border-radius: 0.3rem;
                cursor: pointer;
                color:black;
            ''',
            'accept':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        }),required=True, validators=[
            FileExtensionValidator(allowed_extensions=['docx']),
        ])
    class Meta:
        model = File
        fields = ["file"]



