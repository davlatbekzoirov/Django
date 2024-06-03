from django.shortcuts import render
from .forms import ScheduleForm
import openpyxl
from django.http import JsonResponse
import datetime

def schedule_dashboard(request):
    return render(request, 'dashboard.html')


def schedule_view(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            schedule_file = request.FILES['file']
            sheets_data = parse_schedule(schedule_file)
            sheet_name = request.POST.get('sheet_name', list(sheets_data.keys())[0])
            schedule_data = sheets_data[sheet_name]

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'schedule_data': schedule_data})
            context = {
                'form': form,
                'schedule_file':schedule_file,
                'sheets_data': sheets_data,
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
    sheets_data = {}

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        schedule = []
        for row in ws.iter_rows(values_only=True):
            formatted_row = []
            for cell in row:
                if isinstance(cell, datetime.time):
                    formatted_row.append(cell.strftime('%H:%M'))
                elif cell is None:
                    formatted_row.append('')
                else:
                    formatted_row.append(cell)
            schedule.append(formatted_row)
        sheets_data[sheet_name] = schedule

    return sheets_data
