from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import MeetingCreateForm
from .models import Meeting
from django.contrib import messages
from django.views.generic import (
    DetailView,
    ListView)


@staff_member_required
def create(request):
    if request.method == 'POST':
        form = MeetingCreateForm(request.POST)

        if form.is_valid():
            meeting = form.save()
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            messages.success(request, f'Spotkanie {date} o godzinie {time} zostało utworzone pomyślnie!')
            return redirect('meeting_view', pk=meeting.pk)
    else:
        form = MeetingCreateForm()
    return render(request, 'meetings/meeting_create.html', {'form': form})


class MeetingDetailView(LoginRequiredMixin, DetailView):
    model = Meeting


class MeetingListView(LoginRequiredMixin, ListView):
    model = Meeting
    ordering = ['-date', '-time']
