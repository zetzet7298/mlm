from django.shortcuts import render
# Create your views here.

# def create_menus(menu_items, parent_id=0, level=1):
#     menu = []
#     for k, item in enumerate(menu_items):
#         # print(item['parent_id'], parent_id)
#         # sub = []
#         if item['parent_id'] == parent_id:
#             item['level'] = level
#             menu.append(item)
#             create_menus(menu_items, item['id'], level + 1)
            
#     html = '<div class="menu-sub menu-sub-accordion">'
#     html += '</div>'

#     return menu


def index(request):
    return render(request, 'index.html')

def test(request):
    template = loader.get_template('test.html')
    return render(request, 'test.html')