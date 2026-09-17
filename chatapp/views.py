from django.shortcuts import render
from .models import Chat

# Create your views here.
def chat_view(request):
    chats = Chat.objects.all()