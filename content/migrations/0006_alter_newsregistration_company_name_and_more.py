# Generated by Django 5.2.1 on 2025-06-30 23:33

import encrypted_model_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_news_is_registration_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsregistration',
            name='company_name',
            field=encrypted_model_fields.fields.EncryptedCharField(verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='newsregistration',
            name='email',
            field=encrypted_model_fields.fields.EncryptedEmailField(verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='newsregistration',
            name='first_name',
            field=encrypted_model_fields.fields.EncryptedCharField(verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='newsregistration',
            name='last_name',
            field=encrypted_model_fields.fields.EncryptedCharField(verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='newsregistration',
            name='phone',
            field=encrypted_model_fields.fields.EncryptedCharField(verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='newsregistration',
            name='position',
            field=encrypted_model_fields.fields.EncryptedCharField(verbose_name='Должность'),
        ),
    ]
