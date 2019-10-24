from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import MeetingCreateForm, MeetingsRegisterForm
from .models import Meeting
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.views.generic import (
    DetailView,
    ListView)


@staff_member_required
def create(request):
    if request.method == 'POST':
        form = MeetingCreateForm(request.POST)

        if form.is_valid():
            meeting = form.save()
            messages.success(request, f'{meeting.__str__()} zostało utworzone pomyślnie!')
            return redirect('meeting_view', pk=meeting.pk)
    else:
        form = MeetingCreateForm()
    return render(request, 'meetings/meeting_create.html', {'form': form})


def register(request, **kwargs):
    form = MeetingsRegisterForm(request.POST or None)
    codeErrorMsg = 'Błędny kod, spróbuj ponownie!'
    addedToList = 'Zostałeś dodany do listy obecności!'
    existingOnList = 'Już jesteś na liście, nie musisz dopisywać się ponownie :)'
    if request.method == 'GET':
        if 'code' in kwargs:
            if Meeting.objects.filter(is_active=True, **kwargs).exists():
                meeting = Meeting.objects.get(is_active=True, **kwargs)
                if not Meeting.objects.filter(members=request.user, pk=meeting.pk).exists():
                    meeting.members.add(request.user)
                    meeting.save()
                    messages.success(request, f'{meeting.__str__()} zanotowało obecność {request.user}!')
                    messages.info(request, addedToList)
                    return redirect('meeting_view', pk=meeting.pk)
                else:
                    messages.info(request, existingOnList)
                    return redirect('meeting_view', pk=meeting.pk)
            else:
                messages.warning(request, codeErrorMsg)
                return render(request, 'meetings/meeting_register.html', {'form': form})
        else:
            return render(request, 'meetings/meeting_register.html', {'form': form})
    elif request.method == 'POST':
        if Meeting.objects.filter(is_active=True, code=form.data['code']).exists():
            meeting = Meeting.objects.get(is_active=True, code=form.data['code'])
            if not Meeting.objects.filter(members=request.user, pk=meeting.pk).exists():
                if form.is_valid():
                    meeting.members.add(request.user)
                    meeting.save()
                    messages.success(request, f'{meeting.__str__()} zanotowało obecność {request.user}!')
                    messages.info(request, addedToList)
                    return redirect('meeting_view', pk=meeting.pk)
            else:
                messages.info(request, existingOnList)
                return redirect('meeting_view', pk=meeting.pk)
        else:
            messages.warning(request, codeErrorMsg)
            return render(request, 'meetings/meeting_register.html', {'form': form})


@staff_member_required
def activate(request, **kwargs):
    meeting = Meeting.objects.get(pk=kwargs['pk'])
    if meeting.is_active:
        meeting.is_active = False
    else:
        meeting.is_active = True
    meeting.save()
    return redirect('meeting_view', pk=meeting.pk)


@staff_member_required
def delete(request, **kwargs):
    print('in')
    if request.method == 'POST':
        print('if')
        meeting = Meeting.objects.get(pk=kwargs['pk'])
        meeting.delete()
        return redirect('meeting_list')
    print('fuck')


@staff_member_required
def edit(request, **kwargs):
    meeting = Meeting.objects.get(pk=kwargs['pk'])
    form = MeetingCreateForm(request.POST or None)
    if request.method == 'GET':
        form.initial['agenda'] = meeting.agenda
        form.initial['notes'] = meeting.notes
        form.initial['is_active'] = meeting.is_active
        form.initial['date'] = meeting.date.isoformat()
        form.initial['time'] = meeting.time
        return render(request, 'meetings/meeting_edit.html', {'form': form, 'pk': kwargs['pk']})
    elif request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            meeting.agenda = form.cleaned_data['agenda']
            meeting.notes = form.cleaned_data['notes']
            meeting.is_active = form.cleaned_data['is_active']
            meeting.date = form.cleaned_data['date']
            meeting.time = form.cleaned_data['time']
            meeting.save()
            messages.success(request, 'Zmiany zostały zapisane!')
            return render(request, 'meetings/meeting_edit.html', {'form': form, 'pk': kwargs['pk']})


class MeetingDeleteView(PermissionRequiredMixin, DeleteView):
    model = Meeting
    success_url = reverse_lazy('meeting_list')
    permission_required = 'self.is_super'

    def is_super(self, *args, **kwargs):
        return self.request.user.is_superuser()


class MeetingDetailView(LoginRequiredMixin, DetailView):
    model = Meeting

    def post(self, request, *args, **kwargs):
        return redirect('meeting_view', **kwargs)


class MeetingListView(LoginRequiredMixin, ListView):
    model = Meeting
    ordering = ['-date', '-time']
