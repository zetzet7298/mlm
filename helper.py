import re
def check_has_child(menu_items, parent_id):
    for k, item in enumerate(menu_items):
        if item['parent_id'] == parent_id:
            return True
    return False

def create_menus(menu_items, parent_id=0, level=1):
    html = ''
    for k, item in enumerate(menu_items):
        if item['parent_id'] == parent_id:
            is_has_child = check_has_child(menu_items, item['id'])
            icon = '''<span class="menu-icon">
                                <i class="bi bi-people fs-3"></i>
                            </span>''' if level == 1 else ''' <span class="menu-bullet">
                                    <span class="bullet bullet-dot"></span>
                                </span> '''
            #nếu còn child thì khởi tạo thẻ html cha 
            if is_has_child:
                html += f''' 
                <div data-kt-menu-trigger="click" class="menu-item menu-accordion mb-1">
                <span class="menu-link">
                            {icon}
                            <span class="menu-title">{item['name']}</span>
                            <span class="menu-arrow"></span>
                        </span> 
                        <div class="menu-sub menu-sub-accordion">
                        '''
            else:
                html += f'''
                    <div class="menu-item">
                            <a class="menu-link" href="../../demo13/dist/apps/support-center/overview.html">
                                <span class="menu-bullet">
                                    <span class="bullet bullet-dot"></span>
                                </span>
                                <span class="menu-title">{item['name']}</span>
                            </a>
                '''
                
            #đệ quy tìm nạp thẻ con nếu có
            child = create_menus(menu_items, item['id'], level + 1)
            html += child
            
            # nếu là parent thì sẽ có thêm 1 thẻ đóng nữa
            if is_has_child:
                html += '</div>'
            html += '</div>'
    return html

menu_items = [
    {
        'id': 1,
        'name': 'Support Center',
        'parent_id': 0
    },
    {
        'id': 2,
        'name': 'Tickets',
        'parent_id': 1
    },
    {
        'id': 3,
        'name': 'Ticket List',
        'parent_id': 2
    },
    {
        'id': 4,
        'name': 'Overview',
        'parent_id': 1
    },
    {
        'id': 5,
        'name': 'View Ticket',
        'parent_id': 2
    },
    {
        'id': 6,
        'name': 'Sub Ticket',
        'parent_id': 3
    },
]

# results = create_menus(menu_items, 0)
def create_menus2(menu_items, new_list, parent_id=0, level=1):
    cate_child = []
    for k, item in enumerate(menu_items):
        if item['parent_id'] == parent_id:
            cate_child.append(item)
            # del menu_items[k]
    if cate_child:
        new_list.append('<ul>')
        for k, item in enumerate(cate_child):
            new_list.append(rf'<li><a>{item["name"]}</a>')
            create_menus2(menu_items, new_list, item['id'], level + 1)
            new_list.append('</li>')
        new_list.append('</ul>')
    # return html
new_list = []
create_menus2(menu_items, new_list, 0, 1)
print(''.join(new_list))