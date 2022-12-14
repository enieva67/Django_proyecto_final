from django.shortcuts import render
from blog.models import Post, Categoria, Comentario
from .forms import PostsForm, ComentarioForm
from django.views import View
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

def blog(request,posts_id=0):
    pid=posts_id
    posts=Post.objects.all().order_by('-updated')
    return render(request, "blog/blog.html", {"posts": posts,'posts_id':pid})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria,"posts": posts })

def mostrar_comentarios(request,posts_id):
    pid=posts_id
    mostrar_widget=0
    postsel=Post.objects.get(pk=pid)
    postsel.updated=datetime.now()
    postsel.save()
    posts = Post.objects.all().order_by('-updated')
    comentarios=Comentario.objects.filter(posts_id=pid)
    return render(request, "blog/blog.html", {'posts':posts, 'posts_id':pid,'mostrar':mostrar_widget,'comentarios':comentarios})

class Agregar_posts (View):
    def get(self,request):

        formulario_posts = PostsForm()
        return render(request, "blog/formulario.html", {'forms_posts': formulario_posts,})

    def post(self, request):

        formulario_posts = PostsForm(request.POST,request.FILES)

        if formulario_posts.is_valid():
            formulario_posts.save()

        posts = Post.objects.all()
        return render(request, "blog/blog.html", {"posts": posts})

class Agregar_comentario (View):
    def get(self,request,posts_id):
        mostrar_widget=1
        ID = posts_id
        postsel = Post.objects.get(pk=ID)
        postsel.updated = datetime.now()
        postsel.save()
        posts = Post.objects.all().order_by('-updated')

        formulario_com = ComentarioForm()
        return render(request, "blog/blog.html", {'forms_posts': formulario_com,'posts_id':ID,'posts':posts,'mostrar':mostrar_widget})

    def post(self, request,posts_id):
        ID = posts_id
        comentario = Comentario.objects.create(content=request.POST['content'],posts_id=ID, autor=request.user)
        formulario_com = ComentarioForm(instance=comentario)

        if formulario_com.is_valid():
            formulario_com.save()

        posts = Post.objects.all().order_by('-updated')
        return render(request, "blog/blog.html", {"posts": posts})