from django import forms
from django.core.exceptions import ValidationError

# Oy nomlari uchun list
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

class ScheduleForm(forms.Form):
    # Faylni tanlash uchun maydon
    file = forms.FileField(label="Dosya")
    # Boshlang'ich va oxirgi oy uchun maydonlar
    from_month = forms.ChoiceField(choices=MONTH_CHOICES, label="Ay", widget=forms.Select(attrs={'placeholder': 'Ay'}))
    to_month = forms.ChoiceField(choices=MONTH_CHOICES, label="Ay", widget=forms.Select(attrs={'placeholder': 'Ay'}))
    # Ta'til kuni uchun qator maydon
    holidays = forms.MultipleChoiceField(choices=[(i, f'Day {i}') for i in range(1, 8)], widget=forms.CheckboxSelectMultiple, required=False)
    
    # Fayl nomini tekshirish funksiyasi
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file and not file.name.endswith('.xlsx'):
            raise ValidationError("Faqat .xlsx fayllar ruxsat etiladi.")
        return file
    
    # Boshqarish funksiyasi
    def clean(self):
        cleaned_data = super().clean()
        from_month = cleaned_data.get('from_month')
        to_month = cleaned_data.get('to_month')
        if from_month and to_month:
            from_month_index = int(from_month)
            to_month_index = int(to_month)
            if from_month_index > to_month_index:
                raise ValidationError("Boshlang'ich oy oxirgi oydan keyin kelishi mumkin emas.")
        return cleaned_data

