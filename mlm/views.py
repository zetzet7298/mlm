from django.shortcuts import render, redirect
from django.http import JsonResponse
from core.models import MultiLevel
from django.contrib import messages
from django.urls import reverse
import logging
from . import forms

from django.db.models import Count
import helper
logger = logging.getLogger('general')
import re
import json
def check_has_child(menu_items, direct_user_id):

    for k, item in enumerate(menu_items):
        if item['direct_user_id'] == direct_user_id:
            return True
    return False

def create_menus2(menu_items, new_list, direct_user_id=0, level=0):
    cate_child = []
    for k, item in enumerate(menu_items):
        if item['direct_user_id'] == direct_user_id:
            item['level'] = level
            cate_child.append(item)
            # del menu_items[k]
    if cate_child:
        new_list.append('<ul>')
        for k, item in enumerate(cate_child):
            new_list.append(rf'<li><a class="view_detail" href="#" data-id="{item["id"]}" data-full_name="{item["name"]}" data-level="{item["level"]}">{item["name"]}</a>')
            create_menus2(menu_items, new_list, item['id'], level + 1)
            new_list.append('</li>')
        new_list.append('</ul>')

def indirect_calc(items, direct_user_id, level=0):
    total = 0
    for k, item in enumerate(items):
        if item['direct_user_id'] == direct_user_id:
            item['level'] = level
            #bỏ qua ng giới thiệu trực tiếp (con đầu tiên)
            # if item['level'] != 1:
            total += 1
            child = indirect_calc(items, item['id'], level+1)
            total += child
    return total

def calc(items, id):
    user = MultiLevel.objects.filter(id=id).values('direct_user_id', 'indirect_user_id').first()
    direct_user = ''
    indirect_user = ''
    if user:
        direct_user = MultiLevel.objects.filter(id=user['direct_user_id']).values('name').first()
        if direct_user:
            direct_user = direct_user['name']
        indirect_user = MultiLevel.objects.filter(id=user['indirect_user_id']).values('name').first()
        if indirect_user:
            indirect_user = indirect_user['name']
    direct_total = MultiLevel.objects.filter(direct_user_id=id).values('id').count()
    indirect_total = MultiLevel.objects.filter(indirect_user_id=id).values('id').count()
    tiered_total = indirect_calc(items, id)
    direct_total = direct_total * 15
    total = direct_total + indirect_total + tiered_total
    return {
        'direct_user': direct_user, 
        'indirect_user': indirect_user, 
        'direct_total': direct_total, 
        'tiered_total': tiered_total,
        'indirect_total': indirect_total,
        'total': total,
    }

def create_menus(menu_items, direct_user_id=None, level=0):
    # money = 0
    list = []
    for k, item in enumerate(menu_items):
        if item['direct_user_id'] == direct_user_id:
            # item['money'] = calc(menu_items, item['id'])
            # exit()
                # list[direct_user_id]['money'] += 15
            item['level'] = level
            # new_item = {
            #     item['id']: item
            # }
            # list[item['id']] = item
            # if item['direct_user_id']:
            #     list[item['direct_user_id']]['money'] += 15
            #     logger.debug(list[item['direct_user_id']])
            #     logger.debug(list[item['direct_user_id']]['money'])
            list.append(item)
            #đệ quy tìm nạp thẻ con nếu có
            child = create_menus(menu_items, item['id'], level + 1)
            # # logger.debug(child)
            list.extend(child)
            # logger.debug(list[4])
            
            # if item['direct_user_id'] and list and item['direct_user_id'] in list:
                # logger.debug(list)
    # logger.debug(list)
    return list

def index(request):
    objs = MultiLevel.objects.all().values()
    users = MultiLevel.objects.all().values('id', 'name')
    # indirect_users = MultiLevel.objects.all().values('id', 'name')
    # results = create_menus(objs, None, 1)
    multi_levels_test = []
    create_menus2(objs, multi_levels_test, None, 0)
    # test = calc(objs, 3)
    # logger.debug(test)
    context = {
        'multi_levels_test' : ''.join(multi_levels_test),
        'users' : users,
        # 'indirect_users' : indirect_users,
        # 'multi_levels' : results,
    }
    return render(request, 'multi-level/multi_level_index.html', context)

def delete_all(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE `multi_level`")
    # objs = MultiLevel.objects.all().values()
    # for obj in objs:
    #     MultiLevel.objects.filter(direct_user_id=obj['id']).delete()
    #     MultiLevel.objects.filter(indirect_user_id=obj['id']).delete()
    # # MultiLevel.objects.all().delete()
    return render(request, 'multi-level/multi_level_index.html')
    
def detail_as_json(request, id):
    objs = MultiLevel.objects.all().values()
    data = calc(objs, id)
    return JsonResponse(data, safe=False)

def store_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        direct_user_id = request.POST.get('direct_user_id')
        indirect_user_id = request.POST.get('indirect_user_id')
        # if not direct_user_id:
        #     messages.error(request, "Vui lòng chọn người giới thiệu trực tiếp!")
        logger.debug(request.POST)
        logger.debug(name)
        if direct_user_id:
            direct_user = MultiLevel.objects.filter(direct_user_id=direct_user_id).count()
            if direct_user >= 2:
                messages.error(request, "Chỉ được phép giới thiệut trực tiếp cho 2 user")
                return redirect(reverse('multi_level.index'), request=request)
        # if indirect_user_id:
        #     indirect_user = MultiLevel.objects.get(id=indirect_user_id) 
        
        form = MultiLevel(name=name, email=email, password1=password1, password2=password2, direct_user_id=direct_user_id, indirect_user_id=indirect_user_id)
        # logger.debug(form.is_valid())
        
        if form:
            form.save()
            messages.success(request, "Đã tạo!", extra_tags="safe")
            return redirect(reverse('multi_level.index'), request=request)
        else:
            for field in form:
                logger.debug("Field Error:" + field.name)
                logger.debug(field.errors)
            messages.error(request, "Thất bại!")
            return redirect(reverse('multi_level.index'), request=request)
    else:
        form = forms.MultiLevelForm()
    return render(request, 'multi-level/multi_level_index.html', {'form': form})