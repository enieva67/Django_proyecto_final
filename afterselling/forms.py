from django import forms

from afterselling.models import Encuesta


class EncuestaForm(forms.ModelForm):
    class Meta:
        model=Encuesta
        fields=['producto','edades','genero','estudios','opinion','resenia']