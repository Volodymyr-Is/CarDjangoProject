from django.contrib import admin
from game_store_app.models import *

# Register your models here.
admin.site.register(Platform)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Tag)
admin.site.register(Game)