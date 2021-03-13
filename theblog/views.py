from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from members.decorators import authenticated_user

# def home(request):
#     context = {}
#     return render(request, 'home.html', context)


def home_view(request):
    qs = Post.objects.all()
    context = {'posts': qs}
    return render(request, 'home.html', context)


# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
#     # ordering = ['-id']
#     ordering = ['-post_date']


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail_view(request, pk):
    # id = pk
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'post_detail.html', context)


# @login_required
# class AddPostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'add_post.html'
#     # fields = '__all__'

# @login_required
@authenticated_user
def add_post_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'add_post.html', context)


# @login_required
# class UpdatePostView(UpdateView):
#     model = Post
#     form_class = UpdateForm
#     template_name = 'update_post.html'
#     #fields = ['title', 'body']

@authenticated_user
def update_post_view(request, pk):
    post = Post.objects.get(id=pk)
    form = UpdateForm(instance=post)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'update_post.html', context)

# @login_required


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
