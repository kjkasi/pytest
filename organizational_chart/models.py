from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class OrganizationalChart(models.Model):
    """
    Модель для хранения организационной структуры компании
    """
    name = models.CharField(max_length=255, verbose_name="Название должности")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    level = models.IntegerField(default=0, verbose_name="Уровень в иерархии")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Организационная структура"
        verbose_name_plural = "Организационные структуры"


class OrganizationalChartPage(Page):
    """
    Страница для отображения организационной диаграммы
    """
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
