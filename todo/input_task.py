from django import forms
from .models import Task

class TaskForm(forms.Form):
	title=forms.CharField()
	description=forms.CharField(widget=forms.Textarea)

'''
class TaskModelForm(forms.ModelForm):
	class Meta:
		model=Task
		fields=['title', 'desc']

	def clean_title(self, *args, **kwargs):
		instance= self.instance
		title=self.cleaned_data.get('title')
		qs= Task.objects.filter(title__iexact=title)
		return title

'''