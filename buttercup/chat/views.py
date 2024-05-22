from django.shortcuts import render

from django.shortcuts import render
from .models import ChatRoom, ChatMessage

def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

def room(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    messages = ChatMessage.objects.filter(room=room)
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})
