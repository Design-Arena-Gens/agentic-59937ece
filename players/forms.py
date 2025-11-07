from django import forms
from .models import Player, TournamentRegistration

class PlayerRegistrationForm(forms.ModelForm):
    tournament = forms.ChoiceField(required=False)
    consent = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = Player
        fields = ['name', 'date_of_birth', 'gender', 'position', 'photo', 'institution_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to fields
        for field_name, field in self.fields.items():
            if field_name not in ['consent']:
                field.widget.attrs['class'] = 'form-control'
