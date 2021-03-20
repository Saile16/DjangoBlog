from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)


# es algo unico de cada objeto en los post y asi los vamos a identificar
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # el commit es falso para que uan no enviemos la info a la db
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    # print(request.method)#viendo que nos devuelve este request
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
        return render(request, 'blog/post_edit.html', stuff_for_frontend)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # obtenemos el post y actualizamos un post existente
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # usamos redirect para que nos redirija ala pagina com oactualizandola
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)


def post_draft_list(request):
    # Esto pide todos los draft y despues los enviamos al frontend
    # aun sin publicar
    posts = Post.objects.filter(
        published_date__isnull=True).order_by('-created_at')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # llamaos al metodo de publicar de models
    post.publish()
    # esta redireccion lo podemos cambiar a lo que queramos
    return redirect('post_detail', pk=pk)
