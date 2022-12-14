from django import forms

from .models import Post, Comentario


class PostsForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['titulo','contenido','imagen','content','categorias','autor']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=['content']

