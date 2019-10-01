from django import forms
from .models import Meeting


class MeetingCreateForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = ['datetime', 'agenda', 'notes', 'is_active']
        labels = {
            'datetime': 'Czas wydarzenia',
            'agenda': 'Agenda',
            'notes': 'Notatki',
            'is_active': 'Aktywne'
        }