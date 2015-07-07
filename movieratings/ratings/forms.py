from django import forms


class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices=[(x/2, x/2) for x in range(1, 11)])

