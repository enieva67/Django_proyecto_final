from django import  forms
from .models import DataFrame

class EstadisticaForm(forms.ModelForm):
    class Meta:
        model=DataFrame
        fields=['nombre','datos','imagen']