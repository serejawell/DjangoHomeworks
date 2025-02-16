from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from pytils.translit import slugify

from blog.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'context', 'image', 'is_published')
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        if form.is_valid:
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class PostListView(LoginRequiredMixin, ListView):
    model = Post

    def get_queryset(self, *arg, **kwargs):
        queryset = super().get_queryset(*arg, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'context', 'image', 'is_published')

    def form_valid(self, form):
        if form.is_valid:
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
