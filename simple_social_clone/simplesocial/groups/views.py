from django.db import models
from django.db.models import fields
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

from django.core.urlresolvers import reverse
from django.views import generic

from groups.models import Group, GroupMember


class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group