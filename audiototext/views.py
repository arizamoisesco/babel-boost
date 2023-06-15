from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm

import whisper

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["files"])
            return HttpResponseRedirect("")
        
def handle_uploaded_file(file):
    with open("")as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def index(request):
    return HttpResponse(transcribe())

def transcribe():
    model = whisper.load_model("base")
    audio_text = model.transcribe("audiototext/audios/audio5.ogg")
    result = audio_text["text"]
    return result
