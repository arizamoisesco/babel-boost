from django.shortcuts import render
from django.http import HttpResponse

import whisper


def index(request):
    return HttpResponse(transcribe())

def transcribe():
    model = whisper.load_model("base")
    audio_text = model.transcribe("audio5.ogg")
    result = audio_text["text"]
    return result
