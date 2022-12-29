from django.shortcuts import render
from django.http import HttpResponseRedirect
from calendar import Calendar
from datetime import datetime
from .models import Calendar_days, Gallery

def main_site(request):
    return render(request, 'mainsite/main.html')

def gallery_site(request):
    gallery_photo = Gallery.objects.all()
    gallery_photo_list = []
    for i in gallery_photo:
        gallery_photo_list.append(i.upload.name.replace('mainsite/static/gallery/', ''))
    gallery_photo_dict = {'gallery_photo':gallery_photo_list}
    return render(request, 'mainsite/gallery.html', context=gallery_photo_dict)

def price_site(request):
    return render(request, 'mainsite/price.html')

def reviews_site(request):
    return render(request, 'mainsite/reviews.html')

def rules_site(request):
    return render(request, 'mainsite/rules.html')

def contacts_site(request):
    return render(request, 'mainsite/contacts.html')

def calendar_site(request):
    """Функция возвращает календарь и данные о забронированных ДР из БД и вносит их в календарь на нужные даты"""
    name_month = [{'number':1, 'name':'Январь'},{'number':2, 'name':'Февраль'}, {'number':3, 'name': 'Март'}, {'number':4, 'name': 'Апрель'}, {'number':5, 'name': 'Май'}, {'number':6, 'name': 'Июнь'}, {'number':7, 'name': 'Июль'},{'number':8, 'name': 'Август'}, {'number':9, 'name': 'Сентябрь'},{'number':10, 'name': 'Октябрь'}, {'number':11, 'name': 'Ноябрь'}, {'number':12, 'name': 'Декабрь'}]
    name_day = [{'number':1, 'name':'Пн'},{'number':2, 'name':'Вт'}, {'number':3, 'name': 'Ср'}, {'number':4, 'name': 'Чт'}, {'number':5, 'name': 'Пт'}, {'number':6, 'name': 'Сб'}, {'number':7, 'name': 'Вс'}]
    year_now=datetime.now().year

    if request.POST.__contains__('select_time') and request.POST.__contains__('select_date'):
        """Выбор даты и времени для брони ДР"""
        select_time = request.POST['select_time']
        select_date = request.POST['select_date']
        select_date= datetime.strptime(select_date, '%Y-%m-%d').date()
        return HttpResponseRedirect(f'https://wa.me/+79884718571?text=Добрый%20день.%20Хочу%20забронировать%20праздник%20{select_date.day}.{select_date.month}.{select_date.year}%20на%20{select_time}')

    if request.POST.__contains__('previous_month'):
        """Переключение на предыдущий месяц"""
        cal = Calendar()
        hb = Calendar_days.objects.all().order_by('date_birthday', 'time_birthday_start')
        month_number = int(request.POST['previous_month'])
        year_number=int(request.POST['year'])
        if month_number==1:
            month_number=13
            year_number=year_number-1
        month_number=month_number-1
        cal_dict = {'cal': cal.itermonthdates(year_number, month_number), 'month':month_number,'hb':hb, 'year':year_number, 'name_month':name_month, 'name_day':name_day}
        return render(request, 'mainsite/calendar.html', context=cal_dict)

    elif request.POST.__contains__('next_month'):
        """Переключение на следующий месяц"""
        cal = Calendar()
        hb = Calendar_days.objects.all().order_by('date_birthday', 'time_birthday_start')
        month_number = int(request.POST['next_month'])
        year_number = int(request.POST['year'])
        if month_number==12:
            month_number=0
            year_number=year_number+1
        month_number = month_number + 1
        cal_dict = {'cal': cal.itermonthdates(year_number, month_number), 'month':month_number,'hb':hb, 'year':year_number, 'name_month':name_month, 'name_day':name_day}
        return render(request, 'mainsite/calendar.html', context=cal_dict)
    cal = Calendar()
    hb=Calendar_days.objects.all().order_by('date_birthday', 'time_birthday_start')
    month_number = datetime.now().month
    cal_dict= {'cal':cal.itermonthdates(year_now, month_number), 'month':month_number,'hb':hb, 'year':year_now, 'name_month':name_month, 'name_day':name_day}
    return render(request, 'mainsite/calendar.html', context=cal_dict)


