from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.admin.views.decorators import staff_member_required


from django.views import View
from django.views.generic import (
    edit,
    DetailView,
    ListView)

from .models import Profile
from .forms import UserForm


def login(request):
    if request.user.is_anonymous:
        return render(request, 'members/login.html')
    else:
        return redirect('meeting_list')


@method_decorator(login_required, name="dispatch")
class IndexView(LoginRequiredMixin, ListView):
    template_name = 'members/member_list.html'
    model = User
    context_object_name = 'member_list'


@method_decorator(login_required, name="dispatch")
class DetailView(LoginRequiredMixin, DetailView):
    template_name = 'members/member_detail.html'
    model = User
    context_object_name = 'member'


@method_decorator(staff_member_required, name="dispatch")
class EditView(LoginRequiredMixin, edit.UpdateView):
    template_name = 'members/member_edit.html'
    model = User
    context_object_name = 'member'
    form_class = UserForm

    def form_valid(self, form):
        form.save()
        return redirect('member_list')


@method_decorator(staff_member_required, name="dispatch")
class DeleteView(LoginRequiredMixin, edit.DeleteView):
    template_name = 'members/member_delete.html'
    model = User
    context_object_name = 'member'
    success_url = reverse_lazy('member_list')
