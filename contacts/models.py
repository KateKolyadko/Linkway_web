from django.db import models

class PartnershipRequest(models.Model):
    partner_name = models.CharField("Наименование партнера", max_length=200)
    email = models.EmailField("Электронная почта")
    address = models.TextField("Адрес")
    source = models.CharField("Как вы нас нашли?", max_length=255)  
    comments = models.TextField("Комментарии", blank=True)
    subscribe_newsletter = models.BooleanField("Получать рассылку", default=False)
    agree_terms = models.BooleanField("Согласие с условиями", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка на партнерство"
        verbose_name_plural = "Заявки на партнерство"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка от {self.partner_name}"