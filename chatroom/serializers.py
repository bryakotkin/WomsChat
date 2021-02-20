from rest_framework import serializers
from django.contrib.auth.models import User

from chatroom.models import Room, Chat


class UserSerializers(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    creater = UserSerializers()
    invited = UserSerializers(many=True)

    class Meta:
        model = Room
        fields = ("creater", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация диалогов"""
    user = UserSerializers()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ("room", "text")
