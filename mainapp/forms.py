from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title",max_length=200)
    description = forms.CharField(label="Description")
    reward = forms.FloatField(label="Reward")