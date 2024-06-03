from django import forms
from django.core.exceptions import ValidationError

MONTH_CHOICES = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
]

SEMESTER_CHOICES = [
    ('1', 'Semester 1'),
    ('2', 'Semester 2'),
]

class ScheduleForm(forms.Form):
    file = forms.FileField(label="Dosya")
    semestr = forms.ChoiceField(choices=SEMESTER_CHOICES, label="Yarıyıl", widget=forms.Select(attrs={'placeholder': 'Yarıyılı seç'}))
    year = forms.IntegerField(label="Yıl", widget=forms.NumberInput(attrs={'placeholder': 'Yılı seç'}))
    from_month = forms.ChoiceField(choices=MONTH_CHOICES, label="Ay", widget=forms.Select(attrs={'placeholder': 'Ay'}))
    to_month = forms.ChoiceField(choices=MONTH_CHOICES, label="Ay", widget=forms.Select(attrs={'placeholder': 'Ay'}))

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith('.xlsx'):
                raise ValidationError("Only .xlsx files are allowed.")
        return file

    def clean(self):
        cleaned_data = super().clean()
        from_month = cleaned_data.get('from_month')
        to_month = cleaned_data.get('to_month')

        if from_month and to_month:
            from_month_index = int(from_month)
            to_month_index = int(to_month)
            if from_month_index > to_month_index:
                raise ValidationError("The start month cannot be later than the end month.")

        return cleaned_data