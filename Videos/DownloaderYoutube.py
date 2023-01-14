from pytube import YouTube
import os

liga = str(input("Liga del video de YouTube: "))

def menu():
    print("Bienvenido al descargador de videos de YouTube, ¿que quieres hacer?")
    print("--- [Menu] ---")
    print("[1] Descargar .mp4")
    print("[2] Descargar .mp3")
    print("[3] Descargar .wav")
    print("[0] Salir")
menu()

def opc1(liga):
    yt = YouTube(liga)
    descarga = yt.streams.get_highest_resolution()
    descarga.download()

def opc2(liga):
    yt = YouTube(liga)
    video = yt.streams.filter(only_audio=True).first()
    descarga = video.download()
    base, ext = os.path.splitext(descarga)
    new_file = base + '.mp3'
    os.rename(descarga, new_file)
    
def opc3(liga):
    yt = YouTube(liga)
    video = yt.streams.filter(only_audio=True).first()
    descarga = video.download()
    base, ext = os.path.splitext(descarga)
    new_file = base + '.wav'
    os.rename(descarga, new_file)
    
    
opc = int(input("Seleccione alguna opción: "))
while opc != 0:
    if (opc == 1):
        opc1(liga)
    elif(opc == 2):
        opc2(liga)
    elif(opc == 3):
        opc3(liga)
    else:
        print("Opción invalida")
    print()
    menu()
    opc = int(input("Seleccione alguna opción: "))
print("¡Adios! ")

