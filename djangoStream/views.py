import time

from django.shortcuts import render
from django.http import StreamingHttpResponse

def home(request):
    return render(request, 'home.html')


def custom_ai_logic():
    for i in range(1, 11):
        yield f"Chunk {i} <br>"
        time.sleep(1)


def streaming_view(request):
    response = StreamingHttpResponse(custom_ai_logic(),  content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response




