import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jd = json.load(jfile)

    for menu in jd['menu']:
        menu_id = menu['id']
        menu_align = menu['align']
        menu_items = menu['items']
        for menu_items in jd['menu'][0]['items']:
            menu_items_id = menu_items['id']
            menu_items_display = menu_items['display']
            for menu_items_items in jd['menu'][0]['items'][0]['items']:
                menu_items_items_id = menu_items_items['id']
                menu_items_items_display = menu_items_items['display']
                menu_items_items_link = menu_items_items['link']
                print(menu_items_items_id)
                print(menu_items_items_display)
                print(menu_items_items_link)
            print(menu_items_id)
            print(menu_items_display)
        print(menu_id)
        print(menu_align)