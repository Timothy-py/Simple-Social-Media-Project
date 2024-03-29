from django.shortcuts import render
from django.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView
from braces.views import SelectRelatedMixin         # *****
from django.contrib.auth import get_user_model
from . import models
from . import forms

# POSTS VIEWS.PY FILE
# Create your views here.

class PostList(SelectRelatedMixin, ListView):
    model =  models.Post
    select_related = ('user', 'group')          # *****


class UserPosts(ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(username__ixact=self.kwargs.get('username'))    # *****
        except Username.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all

    def get_context_data(self, **kwargs):           # what is this method?
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__ixact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    fields = ('message', 'group')
    model = models.Post
    # form_class =

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):

    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:post_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
