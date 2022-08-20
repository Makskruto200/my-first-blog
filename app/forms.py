from .models import Apps
from django.forms import ModelForm, TextInput, Textarea


class AppsForm(ModelForm):
    class Meta:
        model = Apps
        fields = ['name', 'text', 'file', 'img', 'video']
        widgets = {
            'name': TextInput(attrs={
                'class': "text",
            }),

            'text': Textarea(attrs={
                'class': 'text',
            }),

        }
