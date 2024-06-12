from django.forms import ModelForm, TextInput
from .models import Add_jobs, AdminMessage

class AdminMessageForm(ModelForm):
    class Meta:
        model = AdminMessage
        fields = ['message']
class MyForm(ModelForm):
    class Meta:
        model = Add_jobs
        fields = ["link", "name"]

        widgets = {
            "link": TextInput(attrs={
                "class": "input",
                "placeholder": "Link"
            }),
            "name": TextInput(attrs={
                "class": "input",
                "placeholder" : "Name"
            })
        }