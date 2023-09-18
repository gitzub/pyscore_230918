from django.contrib import admin

# Register your models here.
from .models import Gamelist, Score, Rankname, Part


class ScoreInline(admin.TabularInline):
    model = Score
    extra = 3


class GamelistAdmin(admin.ModelAdmin):
    list_display = ("gamedate", "gamememo")
    inlines = [ScoreInline]


admin.site.register(Gamelist, GamelistAdmin)
admin.site.register(Score)
admin.site.register(Part)
admin.site.register(Rankname)
