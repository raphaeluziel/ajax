from django.contrib import admin

from .models import Player, Category, Question, Answer

admin.site.register(Player)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
