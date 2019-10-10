from django import forms
from .models import Meeting, Attendance


class MeetingCreateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data spotkania")
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Godzina spotkania")

    class Meta:
        model = Meeting
        fields = ['date', 'time', 'agenda', 'notes', 'is_active']
        labels = {
            'agenda': 'Agenda',
            'notes': 'Notatki',
            'is_active': 'Aktywne'
        }


class MeetingsRegisterForm(forms.ModelForm):
    code = forms.CharField(max_length=32, label='Kod')

    class Meta:
        model = Meeting
        fields = ['code']
