# birthday_problem/forms.py

from django import forms

class BirthdayProblemForm(forms.Form):
    n_students = forms.IntegerField(label='Number of People', min_value=2, max_value=100, initial=23)
    perturbation = forms.FloatField(label='Perturbation Factor', min_value=0.0, max_value=1.0, initial=0.1)
