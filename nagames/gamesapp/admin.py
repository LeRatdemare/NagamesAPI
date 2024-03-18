from django.contrib import admin
from gamesapp.models import GameSession

# Register your models here.
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin', 'creation_date', 'active')

admin.site.register(GameSession, GameSessionAdmin)