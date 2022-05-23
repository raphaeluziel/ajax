from django import forms

from .models import Category

class AjaxForm(forms.Form):
    player_pk = forms.IntegerField(min_value=0)
    category_pk = forms.IntegerField(min_value=0)
    question_pk = forms.IntegerField(min_value=0)
    answer_pk = forms.IntegerField(min_value=0)
