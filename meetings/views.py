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
            time = form.cleaned_data.get('datetime')
            messages.success(request, f'Spotkanie {time} zostało utworzone pomyślnie!')
            return redirect('meeting_view', id=meeting.pk)
    else:
        form = MeetingCreateForm()
    return render(request, 'meetings/meeting_create.html', {'form': form})


class MeetingDetailView(DetailView):
    model = Meeting
