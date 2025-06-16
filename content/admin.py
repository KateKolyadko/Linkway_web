from django.contrib import admin
from .models import Vendor, News, NewsCategory, VendorCategory, NewsRegistration


@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    ordering = ("order",)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "website", "display_categories") 
    search_fields = ("name", "slug")
    list_filter = ("categories",)  
    filter_horizontal = ("categories",)  
    prepopulated_fields = {"slug": ("name",)}
    
    fieldsets = (
        ("Основное", {
            "fields": ("name", "slug", "logo", "website", "short_description")
        }),
        ("Контент", {
            "fields": ("description",)
        }),
        ("Сортировка", {
            "fields": ("order", "categories") 
        }),
    )

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = "Категории"


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class NewsRegistrationInline(admin.TabularInline):
    """Регистрации прямо в админке новости"""
    model = NewsRegistration
    extra = 0
    readonly_fields = ('created_at',)
    fields = ('created_at', 'last_name', 'first_name', 'company_name', 'email', 'phone', 'position')
    ordering = ('-created_at',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'registrations_count')
    inlines = [NewsRegistrationInline]
    
    def registrations_count(self, obj):
        return obj.registrations.count()
    registrations_count.short_description = 'Регистраций'

@admin.register(NewsRegistration)
class NewsRegistrationAdmin(admin.ModelAdmin):
    list_display = ('news', 'last_name', 'first_name', 'company_name', 'created_at')
    list_filter = ('news', 'created_at')
    search_fields = ('last_name', 'first_name', 'company_name', 'email', 'news__title')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        (None, {
            'fields': ('news', 'created_at')
        }),
        ('Информация о участнике', {
            'fields': (
                ('last_name', 'first_name'),
                'position',
                'company_name',
                ('email', 'phone')
            )
        }),
    )