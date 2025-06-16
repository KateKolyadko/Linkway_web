from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ProjectProposalForm
from content.models import News, Vendor 
import os
import traceback

def home(request):
    if request.method == 'POST':
        print("Request FILES:", request.FILES)  
        
        form = ProjectProposalForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                instance = form.save()
                
                print(f"Instance saved: ID={instance.id}")
                if instance.attachment:
                    print(f"Attachment saved: {instance.attachment.name}")
                    file_path = os.path.join(settings.MEDIA_ROOT, instance.attachment.name)
                    print(f"File path: {file_path}")
                    print(f"File exists: {os.path.exists(file_path)}")
                else:
                    print("No file attached")
                
                messages.success(request, "Заявка успешно отправлена!")
                return redirect('home')
            except Exception as e:
                error_msg = f"Ошибка при сохранении: {str(e)}"
                print(error_msg)
                traceback.print_exc() 
                messages.error(request, error_msg)
        else:
            error_messages = []
            for field, errors in form.errors.items():
                field_name = form.fields[field].label if field in form.fields else field
                for error in errors:
                    error_messages.append(f"{field_name}: {error}")
            
            main_error = "Ошибка при отправке формы. Пожалуйста, проверьте данные."
            detailed_error = "<br>".join(error_messages)
            
            print("Form errors:", detailed_error)
            messages.error(request, main_error)
            messages.error(request, detailed_error)
    else:
        form = ProjectProposalForm()
    
    latest_news = News.objects.all().order_by('-pub_date')[:3]
    vendors = Vendor.objects.all().order_by('order')[:8]  
    all_vendors = Vendor.objects.all().order_by('name')
    
    context = {
        'form': form,
        'latest_news': latest_news,
        'vendors': vendors,
        'all_vendors': all_vendors,
    }
    
    return render(request, 'main.html', context)