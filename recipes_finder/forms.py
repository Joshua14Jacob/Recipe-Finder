# forms.py

from django import forms

class InputForm(forms.Form):
    user_input = forms.CharField(label='Enter Ingredients', max_length=1000)
