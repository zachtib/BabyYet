from django import forms

from .models import Baby


class UpdateBabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['born', 'name', 'due_date', 'born_on']
        widgets = {
            'due_date': forms.TextInput(
                attrs={'type': 'date'}
            ),
            'born_on': forms.TextInput(
                attrs={'type': 'datetime-local'}
            ),
        }
