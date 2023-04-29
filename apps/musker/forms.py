from django import forms

from apps.musker.models import Meeps


class MeepForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder": "Enter Your Musker Meep!",
                                   "class": "form-control",
                               }
                           ),
                           label='')

    class Meta:
        model = Meeps
        exclude = ('user',)
