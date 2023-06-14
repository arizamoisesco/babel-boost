import whisper

model = whisper.load_model("base")
result = model.transcribe("audio5.ogg")
print(result["text"])