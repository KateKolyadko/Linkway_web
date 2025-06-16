from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field  

class VendorCategory(models.Model):
    """Классы/категории для сортировки вендоров"""
    name = models.CharField("Название категории", max_length=100, unique=True)
    order = models.PositiveIntegerField("Порядок сортировки", default=0)

    class Meta:
        verbose_name = "Категория вендора"
        verbose_name_plural = "Категории вендоров"
        ordering = ['order']

    def __str__(self):
        return self.name


class Vendor(models.Model):
    """Модель вендора"""
    name = models.CharField("Название", max_length=200, unique=True)
    slug = models.SlugField("URL-адрес", unique=True, blank=True)
    logo = models.ImageField("Логотип", upload_to="vendors/logos/")
    website = models.URLField("Сайт", blank=True)
    short_description = models.TextField("Краткое описание", max_length=300)
    description = CKEditor5Field("Полное описание", config_name='extends')
    order = models.PositiveIntegerField("Порядок сортировки", default=0)
    categories = models.ManyToManyField(
        VendorCategory,
        verbose_name="Категории для сортировки",
        blank=True
    )

    class Meta:
        verbose_name = "Вендор"
        verbose_name_plural = "Вендоры"
        ordering = ['order', 'name']  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class NewsCategory(models.Model):
    """Категории новостей"""
    name = models.CharField("Название категории", max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class News(models.Model):
    """Модель новости"""
    title = models.CharField("Заголовок", max_length=200)
    background = models.ImageField("Фон", upload_to="news/backgrounds/", blank=True)
    content = CKEditor5Field("Описание", config_name='extends')  
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    event_date = models.DateTimeField("Дата проведения", null=True, blank=True)
    categories = models.ManyToManyField(NewsCategory, verbose_name="Категории")
    

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class NewsRegistration(models.Model):
    """Регистрации на мероприятия в новостях"""
    news = models.ForeignKey(
        News,
        verbose_name="Новость",
        related_name="registrations",
        on_delete=models.CASCADE
    )
    company_name = models.CharField("Название компании", max_length=200)
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Номер телефона", max_length=20)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    position = models.CharField("Должность", max_length=150)
    created_at = models.DateTimeField("Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Регистрация на новость"
        verbose_name_plural = "Регистрации на новости"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.company_name})"