from django.db import models

class Calendar_days(models.Model):
    time_choises = [('10:00','10:00'),('11:00','11:00'),('12:00','12:00'),('13:00','13:00'),('14:00','14:00'),('15:00','15:00'),('16:00','16:00'),('17:00','17:00'),('18:00','18:00'),('19:00','19:00'),('20:00','20:00'),('21:00','21:00'),]
    name_par = models.CharField(max_length=30,  null=False, verbose_name='ФИО родителя:')
    phone = models.IntegerField(null=False, verbose_name='Телефон родителя:')
    name_child = models.CharField(max_length=30, null=False, verbose_name='ФИО ребенка:')
    date_birthday = models.DateField(verbose_name='Дата мероприятия:')
    time_birthday_start = models.CharField(max_length=10, null=True, verbose_name='Время начала:', choices=time_choises)
    time_birthday_end = models.CharField(max_length=10, null=True, verbose_name='Время завершения:',choices=time_choises)
    comment = models.TextField(max_length=200, blank=True, null=True, verbose_name='Дополнительная информация:')

    def __str__(self):
        return f'Сопровождающий: {self.name_par}, тел: {self.phone}, дата: {self.date_birthday}, время: {self.time_birthday_start}, именинник: {self.name_child}'

    class Meta:
        verbose_name = u"событие"
        verbose_name_plural = u"События"
        ordering=['date_birthday', 'time_birthday_start']

class Gallery(models.Model):
    upload = models.FileField(upload_to='', verbose_name='Добавить фото')

    def __str__(self):
        name = self.upload.name
        name=name.split('/')
        return f'{name[-1]}'

    class Meta:
        verbose_name = u"фото в галерею"
        verbose_name_plural = u"Галерея"