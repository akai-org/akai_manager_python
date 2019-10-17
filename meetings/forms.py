from django import forms
from .models import Meeting


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'code' in kwargs:
            self.fields['code'] = kwargs['code']

    code = forms.CharField(max_length=32, label='Kod')

    class Meta:
        model = Meeting
        fields = ['code']


class MeetingDetailForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['agenda', 'notes']
        labels = {'agenda': 'Agenda', 'notes': 'Notatki'}
