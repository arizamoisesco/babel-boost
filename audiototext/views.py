from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm

import whisper
import os

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            handle_uploaded_file(file)#Función para guardar el archivo en la carpeta
            text = transcribe(file)
            #return render(request, 'speechtext/upload_success.html', {'text': text})
            return render(request, 'speechtext/upload_success.html', {'text': text})
    else:
        form = UploadFileForm()
    
    return render(request, 'speechtext/uploadForm.html', {'form': form})
        
def handle_uploaded_file(file):
    #Obtener la ruta completa de la carpeta donde deseo guardarla
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audios')

    #Verificar si la carpeta existe de lo contrario crearla
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    #Obtener la ruta completa del archivo a guardar
    print(file.name)
    file_path = os.path.join(folder_path, file.name)
    
    with open(file_path, 'wb')as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def index(request):
    return HttpResponse(transcribe())

def transcribe(audio):
    model = whisper.load_model("base")
    audio_text = model.transcribe(f"audiototext/audios/{audio}")
    result = audio_text["text"]
    return result
