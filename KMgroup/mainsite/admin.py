from django.contrib import admin
from django.db.models import QuerySet
from .models import Calendar_days, Gallery

class MonthFilter(admin.SimpleListFilter):
    title = 'Фильтр по месяцу:'
    parameter_name = 'month'

    def lookups(self, request, model_admin):
        return [('1', 'Январь'),('2', 'Февраль'),('3', 'Март'),('4', 'Апрель'),('5', 'Май'),('6', 'Июнь'),('7', 'Июль'),('8', 'Август'),('9', 'Сентябрь'),('10', 'Октябрь'),('11', 'Ноябрь'),('12', 'Декабрь'),]

    def queryset(self, request, queryset: QuerySet):
        if self.value():
            return queryset.filter(date_birthday__month=self.value())

class YearFilter(admin.SimpleListFilter):
    title = 'Фильтр по году:'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return [('2022', '2022'),('2023', '2023')]

    def queryset(self, request, queryset: QuerySet):
        if self.value():
            return queryset.filter(date_birthday__year=self.value())

class Calendar_daysAdmin(admin.ModelAdmin):
    list_display = ['date_birthday','time_birthday_start','time_birthday_end', 'name_par', 'phone', 'name_child']
    ordering = ['date_birthday','time_birthday_start']
    list_per_page = 20
    search_fields = ['name_par__iregex', 'phone__iregex']
    list_filter = [YearFilter, MonthFilter]

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['upload']

admin.site.register(Calendar_days, Calendar_daysAdmin)
admin.site.register(Gallery)
