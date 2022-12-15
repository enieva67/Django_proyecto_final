from django import  forms
from .models import DataFrame, ClienteEstudio

class EstadisticaForm(forms.ModelForm):
    class Meta:
        model=DataFrame
        fields=['nombre','datos','imagen']


class EstudioClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteEstudio
        fields = ['age', 'annual_income', 'spscore']