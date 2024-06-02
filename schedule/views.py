from django.shortcuts import render
from .forms import ScheduleForm
import openpyxl

def schedule_dashboard(request):
    return render(request, 'dashboard.html')

def schedule_view(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            schedule_file = request.FILES['file']
            schedule_data = parse_schedule(schedule_file)
            context = {
                'form': form,
                'schedule_data': schedule_data,
                'semestr': form.cleaned_data['semestr'],
                'year': form.cleaned_data['year'],
                'from_month': dict(form.fields['from_month'].choices)[form.cleaned_data['from_month']],
                'to_month': dict(form.fields['to_month'].choices)[form.cleaned_data['to_month']],
            }
            return render(request, 'index.html', context)
    else:
        form = ScheduleForm()
    return render(request, 'index.html', {'form': form})

def parse_schedule(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active

    schedule = []
    for row in ws.iter_rows(values_only=True):
        schedule.append([cell if cell is not None else '' for cell in row])

    return schedule
