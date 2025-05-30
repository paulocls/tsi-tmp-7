import whisper
import warnings
from langchain_ollama import OllamaLLM

# Ignorar avisos relacionados ao FP16
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Carregar o modelo Whisper
model = whisper.load_model("large")

audio_path = 'unidade6/record.mp3'

audio = model.transcribe(audio_path)

texto = audio["text"]

print(texto)

#Carregar o resumo do audio

model = OllamaLLM(model='llama3:latest')

resumo = model.invoke(texto)

print(f'O resumo: {resumo}')




