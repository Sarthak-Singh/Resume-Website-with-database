from django.contrib import admin

from .models import About, Social, \
    Skill_category, Skill, \
    Training, \
    Project, \
    Port_Filter, Port_Column, Port_Item, \
    Contact

admin.site.register(About)
admin.site.register(Social)

admin.site.register(Skill_category)
admin.site.register(Skill)

admin.site.register(Training)

admin.site.register(Project)

admin.site.register(Port_Filter)
admin.site.register(Port_Column)
admin.site.register(Port_Item)

admin.site.register(Contact)
