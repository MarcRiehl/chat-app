from django.shortcuts import render
from .models import Chat
import json
from django.http import JsonResponse

# Create your views here.


def chat_view(request):

    if request.method == "GET":

        chats = Chat.objects.all()

        data = []

        for chat in chats:
            data.append({
                "id": chat.id,
                "name": chat.name,
                "message": chat.message,
                "created_at": chat.created_at,
            })

        return JsonResponse(data, safe=False)

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

    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )
