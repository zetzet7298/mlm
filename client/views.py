from django.shortcuts import render, redirect
from . import forms
from .models import *
from django.contrib import messages
from django.urls import reverse
import logging
logger = logging.getLogger('general')

def index(request):
    return render(request, 'client/client_index.html')

def client_type_index(request):
    objs = ClientType.objects.all().values()
    current_path = request.path
    

    context = {
        'client_types' : objs,
        
    }
    return render(request, 'client_type/client_type_index.html', context)

def store_client_type(request):
    if request.method == 'POST':
        form = forms.ClientTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đã tạo!", extra_tags="safe")
            return redirect(reverse('client_type.index'), request=request)
        else:
            messages.error(request, "Thất bại!")
    else:
        form = forms.ClientTypeForm()
    return render(request, 'client/client_index.html', {'form': form})

def delete_client_type(request, id):
    obj = ClientType.objects.get(id=id)
    obj.delete()
    messages.success(request, "Đã xóa!")
    return redirect(reverse('client_type.index'))

def update_client_type(request, id):
    obj = ClientType.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ClientTypeForm(request.POST, instance=obj)
        logger.debug(obj)
        logger.debug(form)
        logger.debug(request.POST)
        if form.is_valid():
            from datetime import datetime
            form.update_date = datetime.now()
            form.save()
            messages.success(request, "Đã cập nhật!", extra_tags="safe")
            return redirect(reverse('client_type.index'), request=request)
        else:
            messages.error(request, "Thất bại!")
    else:
        form = forms.ClientTypeForm()
    return render(request, 'client/client_index.html', {'form': form})