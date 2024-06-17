from pytube import YouTube

def descargar_video():
    try:
        enlace = input('Ingrese el enlace del video o canción: ')
        print('\n')

        yt = YouTube(enlace)
        print("Título del video:", yt.title)
        print("Autor del video:", yt.author)
        print('\n')

        duracion = yt.length
        minutos, segundos = divmod(duracion, 60)
        print(f"Duracióndel video: {minutos:02d}:{segundos:02d}") 

        mejor_calidad = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        ruta_descarga = './' 
        mejor_calidad.download(ruta_descarga) 

        print(f"El video '{yt.title}' ha sido descargado correctamente en '{ruta_descarga}'")

    except Exception as e:
        print(f"Hubo un error al descargar el video: {e}")
        print("Por favor, verifique el enlace e intente de nuevo.")

if __name__ == "__main__":
    descargar_video()
