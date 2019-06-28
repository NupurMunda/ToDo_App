from django import forms

from .models import Task
class AddTaskForm(forms.ModelForm):
	class Meta:
		model= Task
		fields = ('title', 'description','deadline',)

