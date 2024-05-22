from django.db import models

from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
