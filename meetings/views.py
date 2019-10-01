from django.shortcuts import render, redirect
from .forms import MeetingCreateForm
from .models import Meeting
from django.contrib import messages
from django.views.generic import (
    DetailView
)


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


class MeetingDetailView(DetailView):
    model = Meeting
