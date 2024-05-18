# chatbot_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chatbot import ChatbotModel
import json

chat_model = ChatbotModel()

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data['message']
        response = chat_model.get_response(user_message)
        return JsonResponse({"response": response})
    elif request.method == 'GET':
        return render(request, 'chat.html')  # Ensure this line is present and correctly set up
