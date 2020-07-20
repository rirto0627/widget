import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jd = json.load(jfile)

    # for menu in jd['menu']:
    #     menu_id = menu['id']
    #     menu_align = menu['align']
    #     menu_items = menu['items']
    #     for menu_items2 in menu_items:
    #         menu_items_id = menu_items2['id']
    #         menu_items_display = menu_items2['display']
    #
    #         if 'items' in menu_items:
    #             menu_items_items = menu_items2['items']
    #             for menu_items3 in menu_items_items:
    #                 menu_items_items_id = menu_items3['id']
    #                 menu_items_items_display = menu_items3['display']
    #                 menu_items_items_link = menu_items3['link']
    #         elif 'link' in menu_items:
    #             menu_items_link = menu_items2['link']


