from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages
from .forms import NewsRegistrationForm
from .models import Vendor, News, NewsRegistration, VendorCategory
from django.db.models import Q

def vendor_list(request):
    selected_category_id = request.GET.get('category', '')
    categories = VendorCategory.objects.all().order_by('order')
    
    if selected_category_id:
        vendors = Vendor.objects.filter(categories__id=selected_category_id).distinct().order_by('order')
    else:
        vendors = Vendor.objects.all().order_by('order')

    return render(request, 'content/vendor_list.html', {
        'vendors': vendors,
        'categories': categories,
        'selected_category': selected_category_id
    })

def vendor_detail(request, slug):
    vendor = get_object_or_404(Vendor, slug=slug)
    return render(request, 'content/vendor_detail.html', {'vendor': vendor})

def news_list(request):
    category_filter = request.GET.get('category', '')
    latest_news = News.objects.all().order_by('-pub_date')
    
    if category_filter:
        latest_news = latest_news.filter(
            Q(categories__name__iexact=category_filter)
        )
    
    # Фиксированные кнопки для фильтрации
    filter_buttons = [
        {'name': 'Все новости', 'value': ''},
        {'name': 'Мероприятия', 'value': 'Мероприятия'},
        {'name': 'Партнерам', 'value': 'Партнерам'},
        {'name': 'События', 'value': 'События'},
    ]
    
    return render(request, 'content/news_list.html', {
        'latest_news': latest_news,
        'filter_buttons': filter_buttons,
        'current_category': category_filter
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    
    if request.method == 'POST':
        form = NewsRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.news = news
            registration.save()
            messages.success(request, 'Регистрация успешно завершена!')
            return redirect('content:news_detail', pk=news.pk)
    else:
        form = NewsRegistrationForm()
    
    return render(request, 'content/news_detail.html', {
        'news': news,
        'form': form,
        'title': f'{news.title} — Linkway'
    })

class NewsRegistrationsView(ListView):
    model = NewsRegistration
    template_name = 'content/news_registrations.html'
    context_object_name = 'registrations'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return render(request, '403.html', status=403)
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        news_id = self.kwargs['pk']
        return NewsRegistration.objects.filter(news_id=news_id).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = get_object_or_404(News, pk=self.kwargs['pk'])
        return context