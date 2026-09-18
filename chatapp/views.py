from django.shortcuts import render
from .models import Chat
import json
from django.http import JsonResponse

# Create your views here.
def chat_view(request):

    if request.method == "GET":
        chats = Chat.objects.values( #values als Dictionary
            "id",
            "name",
            "message",
            "created_at"
        )
        return JsonResponse(list(chats), safe=False) #umwandlung von QuerySet


    if request.method == "POST":
        data = json.loads(request.body)
        chat = Chat.objects.create(
            name=data["name"],
            message=data["message"]
        )

        return JsonResponse({
            "id": chat.id,
            "name": chat.name,
            "message": chat.message,
            "created_at": chat.created_at
        })