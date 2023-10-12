from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.db.models import Q
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def notice(request):
    if request.GET.get('n'):
        n = request.GET.get('n')
        db = Post.objects.filter(Q(title__icontains=n) | Q(contents__icontains=n)).distinct()
    else:
        db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'notice/notice.html', context)

def secretpost(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'notice/secretpost.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'notice/create.html', {'form': form})

@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'notice/create.html', {'form': form})

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'notice/delete.html', {'post': post})