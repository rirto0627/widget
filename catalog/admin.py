from django.contrib import admin

from .models import widget, Menu, Datetime_Picker, Checkbox_Group, Combo_Box, Text_Input

admin.site.register(widget)
admin.site.register(Menu)
admin.site.register(Datetime_Picker)
admin.site.register(Checkbox_Group)
admin.site.register(Combo_Box)
admin.site.register(Text_Input)
# Register your models here.
