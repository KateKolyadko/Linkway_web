from django.db import models
from encrypted_model_fields.fields import EncryptedCharField, EncryptedEmailField, EncryptedTextField

class PartnershipRequest(models.Model):
    partner_name = EncryptedCharField("Наименование партнера", max_length=200)
    email = EncryptedEmailField("Электронная почта")
    address = EncryptedTextField("Адрес")
    source = EncryptedCharField("Как вы нас нашли?", max_length=255)  
    comments = EncryptedTextField("Комментарии", blank=True)
    subscribe_newsletter = models.BooleanField("Получать рассылку", default=False)
    agree_terms = models.BooleanField("Согласие с условиями", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка на партнерство"
        verbose_name_plural = "Заявки на партнерство"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка от {self.partner_name}"