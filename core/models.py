from django.db import models
from content.models import Vendor
from encrypted_model_fields.fields import EncryptedCharField, EncryptedEmailField, EncryptedTextField

class ProjectProposal(models.Model):
    partner_name = EncryptedCharField("Наименование партнера", max_length=200)
    email = EncryptedEmailField("Электронная почта")
    customer_name = EncryptedCharField("Наименование заказчика", max_length=200)
    vendor = models.ForeignKey(
        Vendor,
        verbose_name="Вендор",
        on_delete=models.CASCADE
    )
    comments = EncryptedTextField("Комментарии", blank=True)
    attachment = models.FileField(
        "Прикрепленный файл",
        upload_to='projects/attachments/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Проект для реализации"
        verbose_name_plural = "Проекты для реализации"
        ordering = ['-created_at']

    def __str__(self):
        return f"Проект от {self.partner_name}"