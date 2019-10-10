from django.shortcuts import render, redirect
from .forms import MeetingCreateForm, MeetingsRegisterForm
from .models import Meeting, Attendance
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


def register(request, **kwargs):
    if Meeting.objects.filter(is_active=True, **kwargs).exists():
        form = MeetingsRegisterForm(request.POST or None, initial=kwargs)

        if form.is_valid():
            meeting = Meeting.objects.get(is_active=True, **kwargs)
            if not Attendance.objects.filter(user=request.user, meeting=meeting).exists():
                attendance = form.save(commit=False)
                attendance.user = request.user
                attendance.meeting = meeting
                attendance.save()
                messages.success(request, f'Spotkanie {meeting.date} o godzinie {meeting.time} zanotowało obecność {request.user}!')
                return redirect('meeting_view', pk=meeting.pk)
            else:
                return redirect('meeting_view', pk=meeting.pk)
    else:
        form = MeetingsRegisterForm()
    return render(request, 'meetings/meeting_register.html', {'form': form})


class MeetingDetailView(DetailView):
    model = Meeting


