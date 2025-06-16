from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PartnershipRequestForm

def partnership_request(request):
    if request.method == 'POST':
        form = PartnershipRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно отправлена!")
            return redirect('contacts:partnership_form')
        else:
            print("Ошибки формы:", form.errors)
            messages.error(request, "Ошибка при отправке. Пожалуйста, проверьте введенные данные.")
    else:
        form = PartnershipRequestForm()
    
    return render(request, 'contacts/partnership_form.html', {'form': form})

def contacts_view(request):
    return render(request, 'contacts/contacts.html')