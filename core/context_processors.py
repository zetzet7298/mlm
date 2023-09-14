import re
from .models import Menu
def check_has_child(menu_items, parent_id):

    for k, item in enumerate(menu_items):
        if item['parent_id'] == parent_id:
            return True
    return False

def create_menus(menu_items, parent_id=None, level=1, path =''):
    html = ''
    for k, item in enumerate(menu_items):
        if item['parent_id'] == parent_id:
            is_has_child = check_has_child(menu_items, item['id'])
            icon = '''<span class="menu-icon"><i class="bi bi-people fs-3"></i></span>''' if level == 1 else '''<span class="menu-bullet"><span class="bullet bullet-dot"></span></span> '''
            #nếu còn child thì khởi tạo thẻ html cha 
            if is_has_child:
                html += f'''<div data-kt-menu-trigger="click" data-id="{item['id']}" class="menu-item menu-accordion mb-1"><span class="menu-link">{icon}<span class="menu-title">{item['name']}</span><span class="menu-arrow"></span></span><div class="menu-sub menu-sub-accordion">'''
            else:
                is_active = 'active' if item['url'] == path else ''
                html += f'''<div data-id="{item['id']}" class="menu-item"><a class="menu-link {is_active}" href="{item['url']}"><span class="menu-bullet"><span class="bullet bullet-dot"></span></span><span class="menu-title">{item['name']}</span></a>'''
                
            #đệ quy tìm nạp thẻ con nếu có
            child = create_menus(menu_items, item['id'], level + 1, path)
            html += child
            id = item['id']
            pattern = rf'(data-id="{id}" class="menu-item menu-accordion mb-1"*)(.*menu-link active)'
            html = re.sub(pattern, r'class="menu-item show menu-accordion mb-1" \2', html)
            # nếu là parent thì sẽ có thêm 1 thẻ đóng nữa
            if is_has_child:
                html += '</div>'
            html += '</div>'
    return html

def get_breadcrumbs_as_html(current_path):
    if current_path:
        breadcrumb = Menu.objects.filter(url = current_path).select_related('parent').first()
        if breadcrumb:
            breadcrumb_name = breadcrumb.name
            breadcrumbs = [breadcrumb]
            breadcrumb_parent = breadcrumb.parent

            while breadcrumb_parent:
                breadcrumb = Menu.objects.filter(id = breadcrumb_parent.id).select_related('parent').first()
                breadcrumbs.insert(0, breadcrumb)
                breadcrumb_parent = breadcrumb.parent
            breadcrumbs_html = f'<h1 class="d-flex align-items-center text-dark fw-bolder fs-3 my-1">{breadcrumb_name}</h1><span class="h-20px border-gray-200 border-start mx-4"></span>'
            breadcrumbs_html += '<ul class="breadcrumb breadcrumb-separatorless fw-bold fs-7 my-1">'
            breadcrumbs_html += '''<li class="breadcrumb-item text-muted">
            <a href="../../demo13/dist/index.html" class="text-muted text-hover-primary">Home</a>
        </li><li class="breadcrumb-item">
            <span class="bullet bg-gray-200 w-5px h-2px"></span>
        </li>'''
            for k, x in enumerate(breadcrumbs):
                if x.url == current_path:
                    breadcrumbs_html += f'''<li class="breadcrumb-item text-dark">{x.name}</li>'''
                else:
                    breadcrumbs_html += f'''<li class="breadcrumb-item text-muted">{x.name}</li>'''
                if k != len(breadcrumbs) -1 :
                    breadcrumbs_html += f'''<li class="breadcrumb-item">
            <span class="bullet bg-gray-200 w-5px h-2px"></span>
        </li>'''
            breadcrumbs_html += '</ul>'
            return breadcrumbs_html
    return ''
def site_settings(request):
    path = request.path
    # from .configs.menu import menu_items
    menu_items = Menu.objects.all().values()
    results = create_menus(menu_items, None, 1, path)
    breadcrumbs_html = get_breadcrumbs_as_html(path)
    context = {
        'menus' : results,
        'breadcrumbs_html': breadcrumbs_html
    }
                        
    return context
