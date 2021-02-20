from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chatroom.models import Room, Chat
from chatroom.serializers import *


class Rooms(APIView):
    """Комнаты чата"""

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})


class Dialog(APIView):
    """Диалоги"""

    permission_classes = [permissions.IsAuthenticated, ]  # только для авторизированных пользователей

    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        dialog = ChatPostSerializers(data=request.data)

        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({"status": "Dialog added"})
        else:
            return Response({"status": "Error! Dialog no added"})
