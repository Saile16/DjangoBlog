from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
# este import es para seguridad que personas sin login no utilicen la app
# agregando @login_required arriba de cada def
from django.contrib.auth.decorators import login_required


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


@login_required
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


@login_required
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
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)


@login_required
def post_draft_list(request):
    # Esto pide todos los draft y despues los enviamos al frontend
    # aun sin publicar
    posts = Post.objects.filter(
        published_date__isnull=True).order_by('-created_at')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # llamaos al metodo de publicar de models
    post.publish()
    # esta redireccion lo podemos cambiar a lo que queramos
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_remove(request, pk):
    # llaamos a comment
    comment = get_object_or_404(Comment, pk=pk)
    # y al delete ya incluido in django
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)
