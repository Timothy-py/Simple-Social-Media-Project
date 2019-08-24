from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import (CreateView,ListView,DetailView)
from Groups.models import Group

# GROUPS VIEWS.PY FILE
# Create your views here.

class CreateGroup(LoginRequiredMixin,CreateView):
    fields = ('name', 'description')
    model = Group

class GroupDetail(DetailView):
    model = Group
    # context_object_name = 'group' DEFAULT >> lowercase of model name

class GroupList(ListView):
    model = Group
