from django.contrib import admin
from chatroom.models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("creater", "invited_users", "date")

    def invited_users(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date")


admin.site.register(Room, RoomAdmin)
admin.site.register(Chat, ChatAdmin)
