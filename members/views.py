from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from django.views.generic import (
    edit,
    DetailView,
    ListView)

from .models import Profile


def login(request):
    if request.user.is_anonymous:
        return render(request, 'members/login.html')
    else:
        return redirect('meeting_list')


@method_decorator(login_required, name="dispatch")
class IndexView(ListView):
    template_name = 'members/member_list.html'
    model = User
    context_object_name = 'member_list'


@method_decorator(login_required, name="dispatch")
class DetailView(DetailView):
    template_name = 'members/member_detail.html'
    model = User
    context_object_name = 'member'


@method_decorator(staff_member_required, name="dispatch")
class DeleteView(edit.DeleteView):
    template_name = 'members/member_delete.html'
    model = User
    context_object_name = 'member'
    success_url = reverse_lazy('member_list')
